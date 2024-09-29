import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import folium
import numpy as np
from streamlit_folium import st_folium
from web3 import Web3
import streamlit.components.v1 as components
from campaign import show_campaigns
from cities import show_cities
from districts import show_districts
from states import show_states
from overview import show_overview

# Title and App Description
st.title("🌧️ India Rainfall & Cloudburst Forecast")
st.markdown("An interactive platform for rainfall monitoring, forecasting, and blockchain-based disaster relief campaigns across India.")

# Sidebar - Selection options
st.sidebar.title("Filter Options")
view_mode = st.sidebar.selectbox("Select View Mode", 
                                 ["India Overview", "State-wise Rainfall", "Major Cities", "West Bengal Districts","Campaign"])

# Whole India Rainfall Visualization - India Map with rainfall data
if view_mode == "India Overview":
    show_overview()
# State-Wise Rainfall Visualization
elif view_mode == "State-wise Rainfall":
    show_states()

# Major Cities Rainfall Visualization
elif view_mode == "Major Cities":
    show_cities()
# West Bengal District-Wise Visualization
elif view_mode == "West Bengal Districts":
    show_districts()

elif view_mode == "Campaign":
    # Blockchain-based Campaign Section
    show_campaigns()