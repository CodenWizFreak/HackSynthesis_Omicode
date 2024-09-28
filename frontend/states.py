import streamlit as st

def show_states():
  st.subheader("State-wise Rainfall")
    
    state = st.sidebar.selectbox("Select State", ["Maharashtra", "West Bengal", "Tamil Nadu", "Kerala", "Delhi", "Karnataka"])
    
    # Fetching state-wise rainfall data (example)
    rainfall_df = pd.DataFrame({
        "District": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
        "Rainfall (mm)": [120, 90, 75, 60, 45]
    })
    
    fig = px.bar(rainfall_df, x="District", y="Rainfall (mm)", title=f"Rainfall in {state}")
    st.plotly_chart(fig)
