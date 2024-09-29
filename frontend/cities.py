import streamlit as st
import pandas as pd
import plotly.express as px

def show_rainfall_by_city(selected_city):
    st.subheader(f"Rainfall Data for {selected_city} in India")

    # Load the dataset
    df = pd.read_csv('frontend\dataset\city_rainfall.csv')  # Update the path to your rainfall data

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    # Filter the dataframe for the selected city's rainfall values
    filtered_df = df[['Date', selected_city]].copy()  # Copy only 'Date' and selected city columns

    # Rename the selected city column for easier reference
    filtered_df.rename(columns={selected_city: 'Rainfall (mm)'}, inplace=True)

    if filtered_df.empty:
        st.error("No data found for the selected city.")
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
                      title=f"Average Daily Rainfall in {selected_city} from {start_date} to {end_date}",
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
    delta_days = {"Upcoming 1 Day": 1, "Upcoming 1 Week": 7, "Upcoming 2 Weeks": 14,
                  "Upcoming 3 Weeks": 21, "Upcoming 1 Month": 30}[time_range]

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

# Function to show top 15 cities
def show_cities():
    st.subheader("Top 15 Cities Rainfall Analysis in India")

    df = pd.read_csv('frontend\dataset\city_rainfall.csv')  # Update the path if needed
    cities = df.columns[1:].tolist()  # Assuming the first column is 'Date' and others are city names

    # Dropdown for selecting the city
    selected_city = st.selectbox("Select a City", cities)

    # Call the function with the selected city
    if selected_city:
        show_rainfall_by_city(selected_city)

    # Initial top cities data
    top_cities_df = pd.DataFrame({
        "City": ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", 
                 "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Surat", 
                 "Kanpur", "Nagpur", "Lucknow", "Visakhapatnam", "Patna"],
        "Average Rainfall (mm)": [240, 800, 900, 900, 1600, 950, 780, 800, 700, 1200, 
                                   800, 900, 1000, 850, 1100, 750]
    })

    # Plot initial rainfall data
    fig = px.bar(top_cities_df, x="City", y="Average Rainfall (mm)", 
                  title="Average Rainfall in Top 15 Cities of India",
                  color="Average Rainfall (mm)", color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig)

    # Show details for the selected city
    city_data = top_cities_df[top_cities_df["City"] == selected_city]
    st.subheader(f"Details for {selected_city}")
    st.markdown(f"**Average Rainfall (mm):** {city_data['Average Rainfall (mm)'].values[0]} mm")

    # Display summary statistics for the selected cities
    total_rainfall = top_cities_df["Average Rainfall (mm)"].sum()
    avg_rainfall = top_cities_df["Average Rainfall (mm)"].mean()
    max_rainfall = top_cities_df["Average Rainfall (mm)"].max()
    max_city = top_cities_df.loc[top_cities_df["Average Rainfall (mm)"].idxmax(), "City"]
    min_rainfall = top_cities_df["Average Rainfall (mm)"].min()
    min_city = top_cities_df.loc[top_cities_df["Average Rainfall (mm)"].idxmin(), "City"]

    st.subheader("Rainfall Data Summary for All Cities")
    st.markdown(f"**Total Rainfall across Cities:** {total_rainfall:.2f} mm")
    st.markdown(f"**Average Rainfall:** {avg_rainfall:.2f} mm")
    st.markdown(f"**City with Maximum Rainfall:** {max_city} ({max_rainfall} mm)")
    st.markdown(f"**City with Minimum Rainfall:** {min_city} ({min_rainfall} mm)")
