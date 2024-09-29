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

frame_dir="frames"
# Function to plot precipitation map for a specific date
def plot_precipitation_map_for_date(date_input="2024_08_31", save_frame=False, frame_idx=None):
    shapefile_path = 'District_shape_West_Bengal.shp'  # Update this to the path of your uploaded .shp file
    india_map = gpd.read_file(shapefile_path)

    # Load the Excel dataset containing precipitation data
    data_path = 'df_wb.xlsx'  # Path to your Excel file
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

    st.subheader(f"Rainfall Data for {selected_district} in West Bengal")

    # Load the dataset
    df = pd.read_csv('frontend\dataset\wb_rainfall_1.csv')  # Update the path if needed

    # Filter the dataframe for the selected district
    filtered_df = df[df['District'].str.lower() == selected_district.lower()]

    if filtered_df.empty:
        st.error("No data found for the selected district.")
        return

    # Convert 'Date' column to datetime if it's not already
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'], format='%Y_%m_%d')

    # Create a time filter for the user
    start_date = st.date_input("Start Date", min_value=filtered_df['Date'].min(), value=filtered_df['Date'].min())
    end_date = st.date_input("End Date", max_value=filtered_df['Date'].max(), value=filtered_df['Date'].max())

    # Filter the data based on date selection
    filtered_rainfall = filtered_df[(filtered_df['Date'] >= pd.to_datetime(start_date)) & 
                                     (filtered_df['Date'] <= pd.to_datetime(end_date))]

    # Plot the rainfall data
    if not filtered_rainfall.empty:
        fig = px.line(filtered_rainfall, 
                      x="Date", 
                      y="Rainfall (mm)",  # Adjust column name as necessary
                      title=f"Average Daily Rainfall in {selected_district} from {start_date} to {end_date}",
                      labels={"Rainfall (mm)": "Rainfall (mm)"})
        st.plotly_chart(fig)
    else:
        st.warning("No rainfall data available for the selected date range.")

    # Calculate summary statistics for the last 14 days
    last_14_days = datetime.now() - timedelta(days=14)
    recent_rainfall = filtered_df[filtered_df['Date'] >= last_14_days]

    if not recent_rainfall.empty:
        total_rainfall = recent_rainfall["Rainfall (mm)"].sum()
        avg_rainfall = recent_rainfall["Rainfall (mm)"].mean()
        max_rainfall = recent_rainfall["Rainfall (mm)"].max()
        max_date = recent_rainfall.loc[recent_rainfall["Rainfall (mm)"].idxmax(), "Date"]
        min_rainfall = recent_rainfall["Rainfall (mm)"].min()
        min_date = recent_rainfall.loc[recent_rainfall["Rainfall (mm)"].idxmin(), "Date"]

        st.subheader("Rainfall Data Summary for the Last 14 Days")
        st.markdown(f"**Total Rainfall (last 14 days):** {total_rainfall} mm")
        st.markdown(f"**Average Rainfall (last 14 days):** {avg_rainfall:.2f} mm")
        st.markdown(f"**Maximum Rainfall (last 14 days):** {max_rainfall} mm on {max_date.strftime('%Y-%m-%d')}")
        st.markdown(f"**Minimum Rainfall (last 14 days):** {min_rainfall} mm on {min_date.strftime('%Y-%m-%d')}")
    else:
        st.warning("No rainfall data available for the last 14 days.")



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
        delta_days = 1
    elif time_range == "Upcoming 1 Week":
        delta_days = 7
    elif time_range == "Upcoming 2 Weeks":
        delta_days = 14
    elif time_range == "Upcoming 3 Weeks":
        delta_days = 21
    elif time_range == "Upcoming 1 Month":
        delta_days = 30

    # Get today's date and calculate the future date
    today = pd.Timestamp.now()
    future_date = today + pd.Timedelta(days=delta_days)

    # Filter for the upcoming time range
    upcoming_rainfall = filtered_df[(filtered_df['Date'] >= today) & (filtered_df['Date'] <= future_date)]

    if not upcoming_rainfall.empty:
        total_rainfall = upcoming_rainfall["Rainfall (mm)"].sum()
        avg_rainfall = upcoming_rainfall["Rainfall (mm)"].mean()
        max_rainfall = upcoming_rainfall["Rainfall (mm)"].max()
        max_date = upcoming_rainfall.loc[upcoming_rainfall["Rainfall (mm)"].idxmax(), "Date"]
        min_rainfall = upcoming_rainfall["Rainfall (mm)"].min()
        min_date = upcoming_rainfall.loc[upcoming_rainfall["Rainfall (mm)"].idxmin(), "Date"]

        st.subheader(f"Rainfall Data Summary for the {time_range}")
        st.markdown(f"**Total Rainfall ({time_range}):** {total_rainfall} mm")
        st.markdown(f"**Average Rainfall ({time_range}):** {avg_rainfall:.2f} mm")
        st.markdown(f"**Maximum Rainfall ({time_range}):** {max_rainfall} mm on {max_date.strftime('%Y-%m-%d')}")
        st.markdown(f"**Minimum Rainfall ({time_range}):** {min_rainfall} mm on {min_date.strftime('%Y-%m-%d')}")
    else:
        st.warning(f"No rainfall data available for the {time_range}.")



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

    # Initial West Bengal district data
    wb_districts_df = pd.DataFrame({
        "District": ["Kolkata", "Howrah", "Darjeeling", "Siliguri", "Durgapur"],
        "Rainfall (mm)": [140, 115, 100, 85, 70]
    })

    # Plot initial rainfall data
    fig = px.bar(wb_districts_df, x="District", y="Rainfall (mm)", title="West Bengal District Rainfall")
    st.plotly_chart(fig)

    # Show details for the selected district
    district_data = wb_districts_df[wb_districts_df["District"] == selected_district]
    st.subheader(f"Details for {selected_district}")
    st.markdown(f"**Rainfall (mm):** {district_data['Rainfall (mm)'].values[0]} mm")

    # Display summary statistics for the selected district
    total_rainfall = wb_districts_df["Rainfall (mm)"].sum()
    avg_rainfall = wb_districts_df["Rainfall (mm)"].mean()
    max_rainfall = wb_districts_df["Rainfall (mm)"].max()
    max_district = wb_districts_df.loc[wb_districts_df["Rainfall (mm)"].idxmax(), "District"]
    min_rainfall = wb_districts_df["Rainfall (mm)"].min()
    min_district = wb_districts_df.loc[wb_districts_df["Rainfall (mm)"].idxmin(), "District"]

    st.subheader("Rainfall Data Summary for All Districts")
    st.markdown(f"**Total Rainfall across Districts:** {total_rainfall} mm")
    st.markdown(f"**Average Rainfall:** {avg_rainfall:.2f} mm")
    st.markdown(f"**District with Maximum Rainfall:** {max_district} ({max_rainfall} mm)")
    st.markdown(f"**District with Minimum Rainfall:** {min_district} ({min_rainfall} mm)")

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

