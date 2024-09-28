import streamlit as st

def show_districts():
  st.subheader("West Bengal District Rainfall")
    
    # West Bengal district data (example)
    wb_districts_df = pd.DataFrame({
        "District": ["Kolkata", "Howrah", "Darjeeling", "Siliguri", "Durgapur"],
        "Rainfall (mm)": [140, 115, 100, 85, 70]
    })
    
    fig = px.bar(wb_districts_df, x="District", y="Rainfall (mm)", title="West Bengal District Rainfall")
    st.plotly_chart(fig)
