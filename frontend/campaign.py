import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_campaigns():
    # Blockchain-based Campaign Section
    st.subheader("🌐 Blockchain Campaigns for Disaster Relief")
    st.markdown("Support blockchain-based campaigns aimed at managing cloudburst and flood relief in India.")
    
    # Example blockchain campaigns data
    campaigns_df = pd.DataFrame({
        "Campaign": ["Flood Relief Mumbai", "Cloudburst Aid Darjeeling", "Disaster Relief Kolkata"],
        "Amount Raised": [50000, 30000, 45000],
        "Goal": [100000, 50000, 80000]
    })
    
    # Display campaign progress
    for i, row in campaigns_df.iterrows():
        st.markdown(f"**{row['Campaign']}**")
        st.progress(row['Amount Raised'] / row['Goal'])
        
    # Bar Chart Visualization
    st.subheader("📊 Fundraising Progress Comparison")
    fig, ax = plt.subplots()
    ax.barh(campaigns_df['Campaign'], campaigns_df['Amount Raised'], color='skyblue')
    ax.set_xlabel('Amount Raised')
    ax.set_title('Funds Raised for Disaster Relief Campaigns')
    st.pyplot(fig)
    
    # Display summary statistics
    total_raised = campaigns_df['Amount Raised'].sum()
    total_goal = campaigns_df['Goal'].sum()
    percentage_complete = (total_raised / total_goal) * 100

    st.markdown(f"**Total Funds Raised:** ₹{total_raised}")
    st.markdown(f"**Total Fundraising Goal:** ₹{total_goal}")
    st.markdown(f"**Overall Progress:** {percentage_complete:.2f}% of total goal reached.")
    
    # Fundraising Section
    st.subheader("💰 Fundraising for Relief Efforts")
    st.markdown("Help us raise funds to manage the impacts of rainfall and cloudbursts across India.")
    
    # User input for suggesting new campaigns
    st.subheader("📝 Suggest a New Campaign")
    new_campaign = st.text_input("Enter the name of the campaign")
    new_goal = st.number_input("Enter the fundraising goal (in ₹)", min_value=1000, step=1000)
    
    if st.button("Add Campaign"):
        if new_campaign and new_goal > 0:
            st.success(f"New campaign '{new_campaign}' with a goal of ₹{new_goal} has been added!")
        else:
            st.error("Please enter valid campaign details.")
    
    # Fundraising Call to Action
    st.subheader("📢 How You Can Help")
    st.markdown("Your contribution, no matter how small, can make a big difference. Click [here](https://www.donate.com) to donate.")
