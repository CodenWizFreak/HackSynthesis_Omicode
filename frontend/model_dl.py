# model.py
import pickle
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def predict(input_list):
    # Ensure the input is a list of 14 numbers
    if len(input_list) != 14:
        raise ValueError("Input list must contain exactly 14 numbers.")

    # Load the pre-trained model
    with open('model/gradient_boosting_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    
    # Reshape the input for the model (assuming the model expects 2D input)
    input_data = [input_list]
    
    # Make the prediction
    prediction = model.predict(input_data)
    prediction_int = int(prediction[0])

    messages = {
        0: ("<span style='color:green;'>Safe: Normal rainfall.</span>", "No precautions needed."),
        1: ("<span style='color:yellow;'>Slight rainfall.</span>", "Be cautious if outdoors."),
        2: ("<span style='color:orange;'>Moderate rainfall.</span>", "Prepare for wet conditions."),
        3: ("<span style='color:red;'>Moderate to heavy rainfall.</span>", "Consider staying indoors."),
        4: ("<span style='color:magenta;'>High rainfall: Prefer to stay home.</span>", "Little risk of cloudburst."),
        5: ("<span style='color:red; font-weight:bold;'>Extreme precaution: Danger.</span>", "Stay indoors and monitor updates."),
    }

    # Display the corresponding message
    if prediction_int in messages:
        message, info = messages[prediction_int]
        st.markdown(message, unsafe_allow_html=True)  # Use markdown to allow HTML
        st.write(info)
    else:
        st.markdown("<span style='color:gray;'>Unknown prediction. Please check the model input.</span>", unsafe_allow_html=True)

    return prediction_int

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from datetime import datetime, timedelta

@st.cache_data
def load_model():
    with open('model/arima_models.pkl', 'rb') as file:
        return pickle.load(file)

arima_models = load_model()

cities = ['Delhi', 'Jaipur', 'Lucknow', 'Kanpur', 'Bhopal', 'Ahmedabad',
          'Surat', 'Nagpur', 'Mumbai', 'Pune', 'Visakhapatnam', 'Hyderabad',
          'Chennai', 'Bengaluru', 'Alipurduar', 'Bankura', 'Birbhum',
          'Dakshin Dinajpur', 'Darjiling', 'Hugli', 'Jalpaiguri', 'Jhargram',
          'Koch Bihar', 'Maldah', 'Murshidabad', 'Nadia', 'North 24 Parganas',
          'Paschim Barddhaman', 'Pashchim Medinipur', 'Purba Barddhaman',
          'Purba Medinipur', 'Puruliya', 'South 24 Parganas', 'Uttar Dinajpur',
          'Kalimpong', 'Haora', 'Kolkata']

# Function to predict rainfall and plot the graph with place and days as parameters
def predict_rain(place, days):
    # Normalize the input city name and match it with the available cities (case insensitive)
    place = place.strip().lower()
    city = next((city for city in cities if city.strip().lower() == place), None)
    
    if not city:
        st.error(f"City '{place}' not found in the model.")
        return
    
    if city not in arima_models:
        st.error(f"No ARIMA model found for '{city}'.")
        return
    
    # Load the model for the selected city
    model = arima_models[city]
    
    # Define the start date for prediction (after 31st August 2024)
    start_date = datetime(2024, 8, 31)
    
    # Generate the forecast for the specified number of days
    forecast = model.forecast(steps=days)
    
    # Create a date range for the forecast
    forecast_dates = [start_date + timedelta(days=i + 1) for i in range(days)]
    
    # Create a DataFrame for the forecast results
    forecast_df = pd.DataFrame({
        'Date': forecast_dates,
        'Rainfall Prediction (mm)': forecast
    })
    
    # Display the predicted data in Streamlit
    st.write(f"Rainfall prediction for {city} for the next {days} days:")
    st.dataframe(forecast_df)
    
    # Plot the forecast results
    st.write("### Rainfall Prediction Graph")
    fig, ax = plt.subplots()
    ax.plot(forecast_df['Date'], forecast_df['Rainfall Prediction (mm)'], marker='o', linestyle='-', color='b')
    ax.set_title(f"Rainfall Prediction for {city} ({days} days)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Predicted Rainfall (mm)")
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Display the plot in Streamlit
    st.pyplot(fig)

   
