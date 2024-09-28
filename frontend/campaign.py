import streamlit as st

def show_campaigns():
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
