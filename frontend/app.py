import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from web3 import Web3
import streamlit.components.v1 as components

# Title and App Description
st.title("🌧️ India Rainfall & Cloudburst Forecast")
st.markdown("An interactive platform for rainfall monitoring, forecasting, and blockchain-based disaster relief campaigns across India.")

# Sidebar - Selection options
st.sidebar.title("Filter Options")
view_mode = st.sidebar.selectbox("Select View Mode", 
                                 ["India Overview", "State-wise Rainfall", "Major Cities", "West Bengal Districts","Campaign"])
date_range = st.sidebar.date_input("Select Date Range", [])

# Whole India Rainfall Visualization - India Map with rainfall data
if view_mode == "India Overview":
    st.subheader("India Rainfall Overview 🌧️")
    
    # Placeholder for Looker Studio (embedded iframe)
    st.markdown("Embedding Looker Studio World Map with India Rainfall data:")
    #st.markdown('<iframe width="100%" height="600px" src="https://lookerstudio.google.com/reporting/53c071aa-7b30-4a09-8d32-cebb22e859f3"></iframe>', unsafe_allow_html=True)
    LOOKER_URL = "https://lookerstudio.google.com/embed/reporting/53c071aa-7b30-4a09-8d32-cebb22e859f3/page/15b2D"
    iframe_code = f"""
    <iframe width="100%" height="1000" src="{LOOKER_URL}" frameborder="0" style="border:0" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>
    """

    # Display the iframe using Streamlit's components.html function
    components.html(iframe_code, height=1000)
# State-Wise Rainfall Visualization
elif view_mode == "State-wise Rainfall":
    st.subheader("State-wise Rainfall")
    
    state = st.sidebar.selectbox("Select State", ["Maharashtra", "West Bengal", "Tamil Nadu", "Kerala", "Delhi", "Karnataka"])
    
    # Fetching state-wise rainfall data (example)
    rainfall_df = pd.DataFrame({
        "District": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "Rainfall (mm)": [120, 90, 75, 60, 45]
    })
    
    fig = px.bar(rainfall_df, x="District", y="Rainfall (mm)", title=f"Rainfall in {state}")
    st.plotly_chart(fig)

# Major Cities Rainfall Visualization
elif view_mode == "Major Cities":
    st.subheader("Major Cities Rainfall")
    
    # Rainfall Data for Major Cities
    cities_df = pd.DataFrame({
        "City": ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"],
        "Rainfall (mm)": [150, 125, 90, 110, 80]
    })
    
    fig = px.scatter(cities_df, x="City", y="Rainfall (mm)", size="Rainfall (mm)", color="City", 
                     title="Rainfall in Major Cities", size_max=60)
    st.plotly_chart(fig)

# West Bengal District-Wise Visualization
elif view_mode == "West Bengal Districts":
    st.subheader("West Bengal District Rainfall")
    
    # West Bengal district data (example)
    wb_districts_df = pd.DataFrame({
        "District": ["Kolkata", "Howrah", "Darjeeling", "Siliguri", "Durgapur"],
        "Rainfall (mm)": [140, 115, 100, 85, 70]
    })
    
    fig = px.bar(wb_districts_df, x="District", y="Rainfall (mm)", title="West Bengal District Rainfall")
    st.plotly_chart(fig)

elif view_mode == "Campaign":
    # Blockchain-based Campaign Section
    st.subheader("🌐 Blockchain Campaigns for Disaster Relief")
    st.markdown("Support blockchain-based campaigns aimed at managing cloudburst and flood relief in India.")

    # Example blockchain campaigns
    campaigns_df = pd.DataFrame({
        "Campaign": ["Flood Relief Mumbai", "Cloudburst Aid Darjeeling", "Disaster Relief Kolkata"],
        "Amount Raised": [50000, 30000, 45000],
        "Goal": [100000, 50000, 80000]
    })

    # Progress bars for campaigns
    for i, row in campaigns_df.iterrows():
        st.markdown(f"**{row['Campaign']}**")
        st.progress(row['Amount Raised'] / row['Goal'])
        
    # Fundraising Section
    st.subheader("💰 Fundraising for Relief Efforts")
    st.markdown("Help us raise funds to manage the impacts of rainfall and cloudbursts across India.")
