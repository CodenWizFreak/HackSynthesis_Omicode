import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from solidity import ether

# Function to display campaigns and allow user to add new ones
def show_campaigns():
    # Initialize session state for storing campaigns
    if "campaigns" not in st.session_state:
        st.session_state.campaigns = pd.DataFrame({
            "Campaign": ["Flood Relief Mumbai", "Cloudburst Aid Darjeeling", "Disaster Relief Kolkata"],
            "Amount Raised": [50000, 30000, 45000],
            "Goal": [100000, 50000, 80000]
        })
    
    # Blockchain-based Campaign Section
    st.subheader("🌐 Blockchain Campaigns for Disaster Relief")

    # Display each campaign with dynamic links (main website and frontend/solidity.py)
    for i, row in st.session_state.campaigns.iterrows():
        campaign_name = row['Campaign']
        st.markdown(f"**{campaign_name}**")
        st.progress(row['Amount Raised'] / row['Goal'])

        # Dynamic links with emojis
        st.markdown(f"[🌐 Website](https://www.mainwebsite.com/{campaign_name.replace(' ', '%20')}) | "
                    f"[📱 Connect via Frontend](http://localhost:8501/frontend/solidity.py?address=Anidipta)")

    # Bar Chart Visualization
    st.subheader("📊 Fundraising Progress Comparison")
    fig, ax = plt.subplots()
    ax.barh(st.session_state.campaigns['Campaign'], st.session_state.campaigns['Amount Raised'], color='skyblue')
    ax.set_xlabel('Amount Raised')
    ax.set_title('Funds Raised for Disaster Relief Campaigns')
    st.pyplot(fig)

    # Display summary statistics
    total_raised = st.session_state.campaigns['Amount Raised'].sum()
    total_goal = st.session_state.campaigns['Goal'].sum()
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
            # Add the new campaign to the DataFrame
            new_row = pd.DataFrame({"Campaign": [new_campaign], "Amount Raised": [0], "Goal": [new_goal]})
            st.session_state.campaigns = pd.concat([st.session_state.campaigns, new_row], ignore_index=True)
            st.success(f"New campaign '{new_campaign}' with a goal of ₹{new_goal} has been added!")
        else:
            st.error("Please enter valid campaign details.")
    
    # Fundraising Call to Action with Dropdown
    st.subheader("📢 How You Can Help")
    st.markdown("Select a name below to connect with our fundraising platform via Frontend/Solidity.")

    # Dictionary to map names to unique IDs
    names_dict = {
        "Ananyo Dasgupta": "XXXXXXXXXXXXX",
        "Anik Bara": "YYYYYYYYYYYYY",
        "Anidipta Pal": "ZZZZZZZZZZZZZ"
    }
    
    # Dropdown list of names
    selected_name = st.selectbox("Choose a Name", list(names_dict.keys()))

    # Display dynamic emoji link for the selected name
    if selected_name:
        unique_id = names_dict[selected_name]
        st.markdown(f"🔗 [📱 Connect with {selected_name} via Frontend](http://localhost:8501/frontend/solidity.py?address={unique_id})")
