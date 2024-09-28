import streamlit as st

def show_overview():
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
