import streamlit as st
import pandas as pd
import plotly.express as px
from model_dl import predict , predict_rain

# Function to show rainfall and predict future conditions based on last 14 days
def show_rainfall_by_city(selected_city):
    st.subheader(f"Rainfall Data for {selected_city} in India")

    # Load the dataset
    df = pd.read_csv('frontend/dataset/city_rainfall.csv')  # Update the path to your rainfall data

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

    # Filter the dataframe for the selected city's rainfall values
    filtered_df = df[['Date', selected_city]].copy()  # Copy only 'Date' and selected city columns
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

    # Plot the rainfall data with markers
    if not filtered_rainfall.empty:
        fig = px.line(filtered_rainfall,
                      x="Date",
                      y="Rainfall (mm)",
                      title=f"Average Daily Rainfall in {selected_city} from {start_date} to {end_date}",
                      labels={"Rainfall (mm)": "Rainfall (mm)"},
                      markers=True)
        st.plotly_chart(fig)
    else:
        st.warning("No rainfall data available for the selected date range.")

    # Dropdown for upcoming rainfall data
    time_range = st.selectbox("Select Time Range for Rainfall Data:", 
                              ["Upcoming 1 Day", "Upcoming 1 Week", "Upcoming 2 Weeks", 
                               "Upcoming 3 Weeks", "Upcoming 1 Month"])

    # Calculate the time delta based on the selected option
    if time_range == "Upcoming 1 Day":
        predict_rain(selected_city, 1)
    elif time_range == "Upcoming 1 Week":
        predict_rain(selected_city, 7)
    elif time_range == "Upcoming 2 Weeks":
        predict_rain(selected_city, 14)
    elif time_range == "Upcoming 3 Weeks":
        predict_rain(selected_city, 21)
    elif time_range == "Upcoming 1 Month":
        predict_rain(selected_city,30)
        
    # Button to ask for weather prediction
    if st.button(f"Predict Future Weather Conditions in {selected_city}"):
        # Collect last 14 days of rainfall data
        recent_rainfall = filtered_rainfall.tail(14)['Rainfall (mm)'].tolist()
        
        # Check if we have exactly 14 days of data
        if len(recent_rainfall) == 14:
            st.subheader(f"Predicted Weather Condition for {selected_city}:")
            prediction = predict(recent_rainfall)
        else:
            st.error("Not enough data available for the last 14 days to make a prediction.")


# Function to show top 15 cities
def show_cities():
    st.subheader("Top 15 Cities Rainfall Analysis in India")

    # Load the dataset
    df = pd.read_csv('frontend/dataset/city_rainfall.csv')  # Update the path if needed
    cities = df.columns[1:].tolist()  # Assuming the first column is 'Date' and others are city names

    # Dropdown for selecting the city
    selected_city = st.selectbox("Select a City", cities)

    # Call the function with the selected city
    if selected_city:
        show_rainfall_by_city(selected_city)
