import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

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

    # Simulated state-wise rainfall data
    rainfall_data = {
        "Andhra Pradesh": np.random.randint(70, 150, 12),
        "Arunachal Pradesh": np.random.randint(100, 200, 12),
        "Assam": np.random.randint(150, 300, 12),
        "Bihar": np.random.randint(30, 90, 12),
        "Chhattisgarh": np.random.randint(50, 120, 12),
        "Goa": np.random.randint(60, 100, 12),
        "Gujarat": np.random.randint(20, 70, 12),
        "Haryana": np.random.randint(40, 80, 12),
        "Himachal Pradesh": np.random.randint(80, 200, 12),
        "Jharkhand": np.random.randint(40, 100, 12),
        "Karnataka": np.random.randint(70, 150, 12),
        "Kerala": np.random.randint(200, 300, 12),
        "Madhya Pradesh": np.random.randint(30, 100, 12),
        "Maharashtra": np.random.randint(40, 130, 12),
        "Manipur": np.random.randint(60, 120, 12),
        "Meghalaya": np.random.randint(200, 350, 12),
        "Mizoram": np.random.randint(100, 180, 12),
        "Nagaland": np.random.randint(50, 100, 12),
        "Odisha": np.random.randint(50, 150, 12),
        "Punjab": np.random.randint(30, 70, 12),
        "Rajasthan": np.random.randint(10, 30, 12),
        "Sikkim": np.random.randint(150, 250, 12),
        "Tamil Nadu": np.random.randint(70, 150, 12),
        "Telangana": np.random.randint(70, 150, 12),
        "Tripura": np.random.randint(60, 120, 12),
        "Uttar Pradesh": np.random.randint(40, 90, 12),
        "Uttarakhand": np.random.randint(80, 200, 12),
        "West Bengal": np.random.randint(100, 200, 12),
        "Delhi": np.random.randint(30, 80, 12),
        "Jammu and Kashmir": np.random.randint(70, 150, 12),
        "Ladakh": np.random.randint(10, 50, 12)
    }

    # Create DataFrame for monthly rainfall
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_rainfall_df = pd.DataFrame({
        "Month": months,
        "Rainfall (mm)": rainfall_data[state]
    })

    # Line chart for monthly rainfall trend
    fig_line = px.line(monthly_rainfall_df, x="Month", y="Rainfall (mm)", title=f"Monthly Rainfall Trend in {state}", markers=True)
    st.plotly_chart(fig_line)

    # Simulated district-wise rainfall data for pie chart
    district_rainfall_data = {
        "District": [f"{state} District {i+1}" for i in range(5)],
        "Rainfall (mm)": np.random.randint(50, 200, 5)
    }
    district_rainfall_df = pd.DataFrame(district_rainfall_data)

    # Pie chart for district rainfall distribution
    fig_pie = px.pie(district_rainfall_df, names='District', values='Rainfall (mm)', title=f"Rainfall Distribution by District in {state}")
    st.plotly_chart(fig_pie)

    # Summary statistics for selected state
    total_rainfall = monthly_rainfall_df["Rainfall (mm)"].sum()
    avg_rainfall = monthly_rainfall_df["Rainfall (mm)"].mean()
    max_rainfall = monthly_rainfall_df["Rainfall (mm)"].max()
    min_rainfall = monthly_rainfall_df["Rainfall (mm)"].min()

    st.subheader("Rainfall Summary Statistics")
    st.markdown(f"**Total Rainfall:** {total_rainfall} mm")
    st.markdown(f"**Average Rainfall:** {avg_rainfall:.2f} mm")
    st.markdown(f"**Maximum Rainfall:** {max_rainfall} mm")
    st.markdown(f"**Minimum Rainfall:** {min_rainfall} mm")
