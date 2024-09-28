import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np 
import streamlit.components.v1 as components

def show_overview():
    st.subheader("India Rainfall Overview 🌧️")

    # Introduction
    st.markdown("""
    Rainfall plays a crucial role in India's agriculture, economy, and overall ecosystem. 
    Understanding rainfall patterns helps in disaster management, water resource allocation, 
    and planning agricultural activities. This overview presents insights into rainfall trends 
    and statistics across different states in India.
    """)

    # Placeholder for Looker Studio (embedded iframe)
    st.markdown("Embedding Looker Studio World Map with India Rainfall data:")
    LOOKER_URL = "https://lookerstudio.google.com/embed/reporting/53c071aa-7b30-4a09-8d32-cebb22e859f3/page/15b2D"
    iframe_code = f"""
    <iframe width="100%" height="600" src="{LOOKER_URL}" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
    """
    # Display the iframe using Streamlit's components.html function
    components.html(iframe_code, height=600)

    # Summary Statistics Section
    st.markdown("### Key Rainfall Statistics")
    
    # Example statistics (replace with actual data as needed)
    rainfall_stats = {
        "Total Average Annual Rainfall": "1,200 mm",
        "Maximum Recorded Rainfall": "1,000 mm (Cherrapunji, Meghalaya)",
        "States with Highest Rainfall": "Maharashtra, Kerala, West Bengal",
        "States with Lowest Rainfall": "Rajasthan, Gujarat"
    }
    
    for key, value in rainfall_stats.items():
        st.markdown(f"**{key}:** {value}")

    # Simulated monthly rainfall data for visualization
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    average_rainfall = np.random.randint(50, 150, size=12)
    monthly_rainfall_df = pd.DataFrame({"Month": months, "Average Rainfall (mm)": average_rainfall})

    # Line chart for monthly rainfall trends
    fig_line = px.line(monthly_rainfall_df, x="Month", y="Average Rainfall (mm)", title="Average Monthly Rainfall in India", markers=True)
    st.plotly_chart(fig_line)

    # Contributing Factors Section
    st.markdown("""
    ### Contributing Factors to Rainfall Patterns in India
    - **Monsoon Seasons**: The Indian monsoon is a vital component of the annual rainfall cycle, 
      bringing heavy rains to most parts of the country between June and September.
    - **Geographical Influences**: The topography of India, including the Western Ghats and Himalayas, 
      significantly influences rainfall patterns, leading to varying amounts of rainfall across regions.
    - **Climate Change**: Increasing temperatures and changing weather patterns are affecting rainfall 
      distribution and intensity, leading to more extreme weather events.
    """)

    # Data Sources Section
    st.markdown("""
    ### Data Sources
    - India Meteorological Department (IMD)
    - National Remote Sensing Centre (NRSC)
    - World Meteorological Organization (WMO)
    """)
