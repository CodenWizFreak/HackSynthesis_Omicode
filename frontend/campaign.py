import streamlit as st

def show_campaigns():
    st.subheader("Campaign Management")
    
    # You can add various functionalities related to campaigns here
    # For example, displaying a list of campaigns
    campaigns = [
        {"name": "Campaign 1", "status": "Active"},
        {"name": "Campaign 2", "status": "Completed"},
        {"name": "Campaign 3", "status": "Pending"}
    ]

    # Display the campaigns in a table
    st.table(campaigns)

    # Add functionality to create a new campaign
    with st.form("new_campaign_form"):
        name = st.text_input("Campaign Name")
        status = st.selectbox("Campaign Status", ["Active", "Completed", "Pending"])
        submit_button = st.form_submit_button("Create Campaign")
        
        if submit_button:
            st.success(f"New campaign '{name}' created with status '{status}'!")
