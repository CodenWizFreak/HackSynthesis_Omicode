import streamlit as st
import pandas as pd
import plotly.express as px

def show_rainfall_by_district(selected_district):
    st.subheader(f"Rainfall Data for {selected_district} in West Bengal")

    # Load the dataset
    df = pd.read_excel('frontend/dataset/df_wb.xlsx')

    # Filter the dataframe for the selected district
    filtered_df = df[df['District'].str.lower() == selected_district.lower()]

    if filtered_df.empty:
        st.error("No data found for the selected district.")
        return

    # Calculate average rainfall if multiple entries exist
    # We will take the mean of the rainfall columns, excluding the 'District' column
    avg_rainfall_df = filtered_df.mean(axis=0, numeric_only=True).reset_index()
    avg_rainfall_df.columns = ['Date', 'Rainfall (mm)']

    # Convert columns (dates) to long format for Plotly
    avg_rainfall_df['Date'] = pd.to_datetime(avg_rainfall_df['Date'], format='%Y_%m_%d')

    # Create a time filter for the user
    start_date = st.date_input("Start Date", min_value=avg_rainfall_df['Date'].min(), value=avg_rainfall_df['Date'].min())
    end_date = st.date_input("End Date", max_value=avg_rainfall_df['Date'].max(), value=avg_rainfall_df['Date'].max())

    # Filter the data based on date selection
    filtered_rainfall = avg_rainfall_df[(avg_rainfall_df['Date'] >= pd.to_datetime(start_date)) & 
                                         (avg_rainfall_df['Date'] <= pd.to_datetime(end_date))]

    # Plot the rainfall data
    if not filtered_rainfall.empty:
        fig = px.line(filtered_rainfall, 
                      x="Date", 
                      y="Rainfall (mm)", 
                      title=f"Average Daily Rainfall in {selected_district} from {start_date} to {end_date}",
                      labels={"Rainfall (mm)": "Rainfall (mm)"})
        st.plotly_chart(fig)
    else:
        st.warning("No rainfall data available for the selected date range.")
        
def show_districts():
    st.subheader("West Bengal District Rainfall")

    df = pd.read_excel('frontend\dataset\df_wb.xlsx')
    districts = df['District'].unique().tolist()

    # Dropdown for selecting the district outside the function
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
