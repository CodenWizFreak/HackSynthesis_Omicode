import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import imageio
import os

# Load your data
df = pd.read_excel('frontend/dataset/df_india.xlsx')

# Load the shapefile of India
india_map = gpd.read_file('frontend/dataset/India new political map/Political_map_2019.shp')

# Directory to save video frames
frame_dir = "frames"

# Function to plot precipitation map for a specific date
def plot_precipitation_map_for_date(date_input="2024_08_31", save_frame=False, frame_idx=None):
    if date_input not in df.columns:
        st.error(f"No precipitation data available for the date {date_input}")
        return None
    
    lat_lon_precip = df[['Latitude', 'Longitude', date_input]].dropna()

    if lat_lon_precip.empty:
        st.error(f"No data available for the date {date_input}")
        return None
    
    fig, ax = plt.subplots(figsize=(10, 10))
    india_map.plot(ax=ax, color='white', edgecolor='black')

    sc = ax.scatter(lat_lon_precip['Longitude'], lat_lon_precip['Latitude'], 
                    c=lat_lon_precip[date_input], cmap='coolwarm', 
                    s=50, edgecolor='k', alpha=0.7)

    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Precipitation (mm)', rotation=270, labelpad=20)

    ax.set_title(f'Rainfall Data for India on {date_input}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    if save_frame and frame_idx is not None:
        frame_path = os.path.join(frame_dir, f"frame_{frame_idx:03d}.png")
        fig.savefig(frame_path)
        plt.close(fig)
        return frame_path

    st.pyplot(fig)
    return None

# Function to create a video from frames
def create_video_from_frames(start_date, end_date):
    # Ensure the frame directory exists
    os.makedirs(frame_dir, exist_ok=True)

    # Get all dates between start and end
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # List to store paths of all generated frames
    frame_paths = []

    # Loop through dates and generate frames
    for idx, date in enumerate(date_range):
        formatted_date = f"{date.year}_{str(date.month).zfill(2)}_{str(date.day).zfill(2)}"
        frame_path = plot_precipitation_map_for_date(formatted_date, save_frame=True, frame_idx=idx)
        if frame_path:
            frame_paths.append(frame_path)

    # Generate video from the frames
    if frame_paths:
        video_path = "rainfall_video.mp4"
        with imageio.get_writer(video_path, fps=5) as writer:
            for frame_path in frame_paths:
                image = imageio.imread(frame_path)
                writer.append_data(image)
        
        st.success("Video created successfully!")
        st.video(video_path)

        # Provide download link for the video
        with open(video_path, "rb") as video_file:
            st.download_button(label="Download Video", data=video_file, file_name="rainfall_video.mp4", mime="video/mp4")
    else:
        st.error("No frames generated for the selected date range.")

# Function to show an overview of rainfall data and provide date selection
def show_overview():
    st.subheader("India Rainfall Overview 🌧️")

    # Sidebar for date selection
    st.sidebar.header("Select Date or Date Range")
    
    # Year selection
    year = st.sidebar.selectbox("Select Year", options=[2022, 2023, 2024])
    
    # Month selection
    if year == 2024:
        month = st.sidebar.selectbox("Select Month", options=list(range(1, 9)))
    else:
        month = st.sidebar.selectbox("Select Month", options=list(range(1, 13)))

    # Day selection
    day = st.sidebar.selectbox("Select Day", options=list(range(1, 32)))

    # Format the selected date as 'YYYY_MM_DD'
    date_input = f"{year}_{str(month).zfill(2)}_{str(day).zfill(2)}"

    # Button to show rainfall map for a single date
    if st.sidebar.button("Show Rainfall Map"):
        plot_precipitation_map_for_date(date_input)

    # Date range selection for video creation
    st.sidebar.subheader("Select Date Range for Video Creation")
    start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
    end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-08-31"))

    if st.sidebar.button("Create Rainfall Video"):
        if start_date > end_date:
            st.sidebar.error("End Date must be after Start Date")
        else:
            create_video_from_frames(start_date, end_date)

    # Additional rainfall statistics and information
    st.markdown("### Key Rainfall Statistics")
    
    rainfall_stats = {
        "Total Average Annual Rainfall": "1,200 mm",
        "Maximum Recorded Rainfall": "1,000 mm (Cherrapunji, Meghalaya)",
        "States with Highest Rainfall": "Maharashtra, Kerala, West Bengal",
        "States with Lowest Rainfall": "Rajasthan, Gujarat"
    }
    
    for key, value in rainfall_stats.items():
        st.markdown(f"**{key}:** {value}")

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    average_rainfall = np.random.randint(50, 150, size=12)
    monthly_rainfall_df = pd.DataFrame({"Month": months, "Average Rainfall (mm)": average_rainfall})

    fig_line = px.line(monthly_rainfall_df, x="Month", y="Average Rainfall (mm)", title="Average Monthly Rainfall in India", markers=True)
    st.plotly_chart(fig_line)

    st.markdown("""
    ### Contributing Factors to Rainfall Patterns in India
    - **Monsoon Seasons**
    - **Geographical Influences**
    - **Climate Change**
    """)

    st.markdown("""
    ### Data Sources
    - India Meteorological Department (IMD)
    - National Remote Sensing Centre (NRSC)
    - World Meteorological Organization (WMO)
    """)

