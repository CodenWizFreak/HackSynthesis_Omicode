import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import imageio
import os

# Load your data
df = pd.read_excel('frontend/dataset/df_india.xlsx')

# Load the shapefile of India
india_map = gpd.read_file('frontend/dataset/India new political map/Political_map_2019.shp')

# Directory to save video frames
frame_dir = "frames"

# Function to plot precipitation for a specific state
def plot_precipitation_map_for_state(state_map, filtered_df, date_str, save_frame=False, frame_idx=None):
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot only the selected state's boundary
    if state_map is not None:
        state_map.plot(ax=ax, color='white', edgecolor='black')

    if filtered_df is not None:
        # Get latitude and longitude for the current state and date
        lat_lon_precip = filtered_df[['Latitude', 'Longitude', date_str]].dropna()

        if not lat_lon_precip.empty:
            # Scatter plot of rainfall data over the state's map
            sc = ax.scatter(lat_lon_precip['Longitude'], lat_lon_precip['Latitude'], 
                            c=lat_lon_precip[date_str], cmap='coolwarm', 
                            s=50, edgecolor='k', alpha=0.7)

            # Add color bar
            cbar = plt.colorbar(sc, ax=ax)
            cbar.set_label('Precipitation (mm)', rotation=270, labelpad=20)

    ax.set_title(f'Rainfall Data for {state_map.iloc[0]["ST_NAME"]} on {date_str}' if state_map is not None else f'Rainfall Data on {date_str}')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    if save_frame and frame_idx is not None:
        frame_path = os.path.join(frame_dir, f"frame_{frame_idx:03d}.png")
        fig.savefig(frame_path)
        plt.close(fig)
        return frame_path

    st.pyplot(fig)
    return None

def create_video_from_frames(start_date, end_date, state_map, filtered_df):
    # Ensure the frame directory exists
    os.makedirs(frame_dir, exist_ok=True)

    # Get all dates between start and end
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # List to store paths of all generated frames
    frame_paths = []

    # Loop through dates and generate frames
    for idx, date in enumerate(date_range):
        formatted_date = f"{date.year}_{str(date.month).zfill(2)}_{str(date.day).zfill(2)}"
        
        # Check if the formatted date is in the columns of the filtered DataFrame
        if formatted_date in filtered_df.columns:
            frame_path = plot_precipitation_map_for_state(state_map, filtered_df, formatted_date, save_frame=True, frame_idx=idx)
            if frame_path:
                frame_paths.append(frame_path)
    else:
        st.warning(f"No data available for {state_map} on {formatted_date}.")

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

# Update the show_states function to restrict years and months
def show_states():
    st.subheader("State-wise Rainfall")

    # List of all 29 states in India
    states = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
        "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
        "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
        "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
        "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand",
        "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh"
    ]
    
    # Sidebar for state selection
    state = st.sidebar.selectbox("Select State", states)
    
    # Filter the DataFrame for the selected state
    filtered_df = df[df['State'] == state]

    # Filter the GeoDataFrame for the selected state
    state_map = india_map[india_map['ST_NAME'] == state]  # Assuming 'ST_NAME' is the column with state names
    
    # Check if there's data for the selected state
    if filtered_df.empty or state_map.empty:
        st.error(f"No rainfall or map data available for {state}.")
        return

    # Dropdown for year selection (restrict to 2022, 2023, 2024)
    year = st.sidebar.selectbox("Select Year", [2022, 2023, 2024])
    
    # Dropdown for month selection based on selected year
    if year == 2024:
        month = st.sidebar.selectbox("Select Month", ["January", "February", "March", "April", "May", 
                                                      "June", "July", "August"])
    else:
        month = st.sidebar.selectbox("Select Month", ["January", "February", "March", "April", "May", 
                                                      "June", "July", "August", "September", "October", 
                                                      "November", "December"])

    # Map month names to their corresponding numerical values
    month_to_num = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    # Get the selected month number
    month_number = month_to_num[month]

    # Dropdown for day selection
    if year == 2024 and month == "August":
        day = st.sidebar.selectbox("Select Day", list(range(1, 32)))  # Until 31st August 2024
    else:
        day = st.sidebar.selectbox("Select Day", list(range(1, 32)))

    # Formatted date string
    date_str = f"{year}_{str(month_number).zfill(2)}_{str(day).zfill(2)}"

    # Check if the selected date exists in the DataFrame
    if date_str in filtered_df.columns:
        # Plot the precipitation map for the specific date with the state's boundary
        plot_precipitation_map_for_state(state_map, filtered_df, date_str)
    else:
        st.warning(f"No data available for {state} on {date_str}.")

    # Date range input for video creation
    st.subheader("Create Video from Date Range")
    
    # Select start and end dates
    start_date = st.date_input("Start Date", value=pd.to_datetime("2022-01-01"))
    if year == 2024:
        end_date = st.date_input("End Date", value=pd.to_datetime("2024-08-31"))
    else:
        end_date = st.date_input("End Date", value=pd.to_datetime("2024-12-31"))

    if st.button("Create Video"):
        create_video_from_frames(start_date, end_date, state_map, filtered_df)        