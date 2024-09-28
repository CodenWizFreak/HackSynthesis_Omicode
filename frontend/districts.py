import streamlit as st
import pandas as pd
import plotly.express as px

def show_districts():
    st.subheader("West Bengal District Rainfall")

    # Initial West Bengal district data
    wb_districts_df = pd.DataFrame({
        "District": ["Kolkata", "Howrah", "Darjeeling", "Siliguri", "Durgapur"],
        "Rainfall (mm)": [140, 115, 100, 85, 70]
    })

    # Plot initial rainfall data
    fig = px.bar(wb_districts_df, x="District", y="Rainfall (mm)", title="West Bengal District Rainfall")
    st.plotly_chart(fig)

    # Dropdown to select a district
    selected_district = st.selectbox("Select a District", wb_districts_df["District"])

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
