import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

def show_cities():
    st.subheader("Rainfall in Cities along the Golden Quadrilateral")

    # Initial Rainfall Data for Major Cities along the Golden Quadrilateral
    cities_df = pd.DataFrame({
        "City": ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"],
        "Rainfall (mm)": [150, 125, 90, 110, 80]
    })

    # Plotly Scatter Plot: Rainfall in Cities
    fig = px.scatter(cities_df, x="City", y="Rainfall (mm)", size="Rainfall (mm)", color="City",
                     title="Rainfall in Major Cities", size_max=60)
    st.plotly_chart(fig)

    # Bar Chart for Rainfall Data using Matplotlib
    st.subheader("Rainfall Comparison - Bar Chart")
    fig, ax = plt.subplots()
    ax.bar(cities_df["City"], cities_df["Rainfall (mm)"], color='orange')
    ax.set_xlabel('City')
    ax.set_ylabel('Rainfall (mm)')
    ax.set_title('Rainfall in Major Cities (Golden Quadrilateral)')
    st.pyplot(fig)

    # Summary Statistics
    total_rainfall = cities_df["Rainfall (mm)"].sum()
    avg_rainfall = cities_df["Rainfall (mm)"].mean()
    max_rainfall = cities_df["Rainfall (mm)"].max()
    max_city = cities_df.loc[cities_df["Rainfall (mm)"].idxmax(), "City"]
    min_rainfall = cities_df["Rainfall (mm)"].min()
    min_city = cities_df.loc[cities_df["Rainfall (mm)"].idxmin(), "City"]

    st.subheader("Rainfall Data Summary")
    st.markdown(f"**Total Rainfall across Cities:** {total_rainfall} mm")
    st.markdown(f"**Average Rainfall:** {avg_rainfall:.2f} mm")
    st.markdown(f"**City with Maximum Rainfall:** {max_city} ({max_rainfall} mm)")
    st.markdown(f"**City with Minimum Rainfall:** {min_city} ({min_rainfall} mm)")

    # Optional User Input: Add More Cities
    st.subheader("📝 Add More Cities to Rainfall Data")
    new_city = st.text_input("Enter the name of the city")
    new_rainfall = st.number_input("Enter the rainfall (in mm)", min_value=0, step=1)

    # Placeholder to dynamically show the new chart after a city is added
    graph_placeholder = st.empty()

    if st.button("Add City"):
        if new_city and new_rainfall > 0:
            # Add the new city data
            new_row = pd.DataFrame({"City": [new_city], "Rainfall (mm)": [new_rainfall]})
            cities_df = pd.concat([cities_df, new_row], ignore_index=True)

            # Display success message and show updated DataFrame
            st.success(f"New city '{new_city}' with rainfall {new_rainfall} mm has been added!")
            st.dataframe(cities_df)

            # Generate updated bar chart with new data
            fig, ax = plt.subplots()
            ax.bar(cities_df["City"], cities_df["Rainfall (mm)"], color='lightblue')
            ax.set_xlabel('City')
            ax.set_ylabel('Rainfall (mm)')
            ax.set_title('Updated Rainfall Data Including New Cities')
            
            # Display the updated graph in the placeholder
            graph_placeholder.pyplot(fig)

        else:
            st.error("Please enter valid city details.")
