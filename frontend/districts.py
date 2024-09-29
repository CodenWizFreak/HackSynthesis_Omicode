import streamlit as st
import pandas as pd
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import imageio
import os
from datetime import datetime, timedelta
from model_dl import predict ,  predict_rain

frame_dir="frames"
# Function to plot precipitation map for a specific date
def plot_precipitation_map_for_date(date_input="2024_08_31", save_frame=False, frame_idx=None):
    shapefile_path = 'frontend\dataset\West Bengal\District_shape_West_Bengal.shp'  # Update this to the path of your uploaded .shp file
    india_map = gpd.read_file(shapefile_path)

    # Load the Excel dataset containing precipitation data
    data_path = 'frontend\dataset\df_wb.xlsx'  # Path to your Excel file
    df = pd.read_excel(data_path)

    # Check if the date column exists in the DataFrame
    if date_input not in df.columns:
        st.error(f"No precipitation data available for the date {date_input}")
        return

    # Select latitude, longitude, and precipitation for the specified date
    lat_lon_precip = df[['Latitude', 'Longitude', date_input]].dropna()

    if lat_lon_precip.empty:
        st.error(f"No data available for the date {date_input}")
        return

    # Set up the figure and axis for plotting
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plot the base map of West Bengal
    india_map.plot(ax=ax, color='white', edgecolor='black')

    # Scatter plot of precipitation data for the specific date
    sc = ax.scatter(lat_lon_precip['Longitude'], lat_lon_precip['Latitude'],
                    c=lat_lon_precip[date_input], cmap='coolwarm',
                    s=300, edgecolor='k', alpha=0.7)

    # Add color bar for precipitation scale
    cbar = plt.colorbar(sc, ax=ax)
    cbar.set_label('Precipitation (mm)', rotation=270, labelpad=20)

    # Set plot title and labels
    ax.set_title(f'Rainfall Data for West Bengal on {date_input}')
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

# Function to display rainfall data by district
def show_rainfall_by_district(selected_district):
    st.subheader(f"Rainfall Data for {selected_district} in West Bengal")

    # Load the dataset
    df = pd.read_csv('frontend/dataset/wb_rainfall.csv')

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    # Filter the dataframe for the selected district's rainfall values
    filtered_df = df[['Date', selected_district]].copy()  # Copy only 'Date' and selected district columns

    # Rename the selected district column for easier reference
    filtered_df.rename(columns={selected_district: 'Rainfall (mm)'}, inplace=True)

    if filtered_df.empty:
        st.error("No data found for the selected district.")
        return

    # Create a time filter for the user
    start_date = st.date_input("Start Date", min_value=filtered_df['Date'].min(), value=filtered_df['Date'].min())
    end_date = st.date_input("End Date", max_value=filtered_df['Date'].max(), value=filtered_df['Date'].max())

    # Filter the data based on date selection
    filtered_rainfall = filtered_df[(filtered_df['Date'] >= pd.to_datetime(start_date)) & 
                                     (filtered_df['Date'] <= pd.to_datetime(end_date))]

    # Plot the rainfall data with each row value spotted by the x-axis Date
    if not filtered_rainfall.empty:
        fig = px.line(filtered_rainfall, 
                      x="Date", 
                      y="Rainfall (mm)",  
                      title=f"Average Daily Rainfall in {selected_district} from {start_date} to {end_date}",
                      labels={"Rainfall (mm)": "Rainfall (mm)"},
                      markers=True)  # Adds markers to each data point
        st.plotly_chart(fig)
    else:
        st.warning("No rainfall data available for the selected date range.")

    # Dropdown for upcoming rainfall data
    time_range = st.selectbox("Select Time Range for Rainfall Data:", 
                              ["Upcoming 1 Day", "Upcoming 1 Week", "Upcoming 2 Weeks", 
                               "Upcoming 3 Weeks", "Upcoming 1 Month"])

    # Calculate the time delta based on the selected option
    if time_range == "Upcoming 1 Day":
        predict_rain(selected_district, 1)
    elif time_range == "Upcoming 1 Week":
        predict_rain(selected_district, 7)
    elif time_range == "Upcoming 2 Weeks":
        predict_rain(selected_district, 14)
    elif time_range == "Upcoming 3 Weeks":
        predict_rain(selected_district, 21)
    elif time_range == "Upcoming 1 Month":
        predict_rain(selected_district,30)

    # Button to ask for weather prediction
    if st.button(f"Predict Future Weather Conditions in {selected_district}"):
        # Collect last 14 days of rainfall data
        recent_rainfall = filtered_rainfall.tail(14)['Rainfall (mm)'].tolist()
        
        # Check if we have exactly 14 days of data
        if len(recent_rainfall) == 14:
            st.subheader(f"Predicted Weather Condition for {selected_district}:")
            prediction = predict(recent_rainfall)
        else:
            st.error("Not enough data available for the last 14 days to make a prediction.")


# Function to show districts
def show_district():
    st.subheader("West Bengal District Rainfall")

    df = pd.read_csv('frontend/dataset/wb_rainfall.csv')  # Update the path if needed
    districts = df.columns[1:].tolist()  # Assuming the first column is 'Date' and others are district names

    # Dropdown for selecting the district
    selected_district = st.selectbox("Select a District", districts)

    # Call the function with the selected district
    if selected_district:
        show_rainfall_by_district(selected_district)


# Streamlit Application Main Logic
def show_districts():
    st.title("West Bengal Rainfall Analysis")

    
    st.header("Precipitation Map")
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
            
    st.header("District Rainfall")
    show_district()

