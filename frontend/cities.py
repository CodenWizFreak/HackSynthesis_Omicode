import streamlit as st

def show_cities():
  st.subheader("Major Cities Rainfall")
    
    # Rainfall Data for Major Cities
    cities_df = pd.DataFrame({
        "City": ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bengaluru"],
        "Rainfall (mm)": [150, 125, 90, 110, 80]
    })
    
    fig = px.scatter(cities_df, x="City", y="Rainfall (mm)", size="Rainfall (mm)", color="City", 
                     title="Rainfall in Major Cities", size_max=60)
    st.plotly_chart(fig)
