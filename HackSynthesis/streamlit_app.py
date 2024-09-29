import streamlit as st
from web3 import Web3
from app.eth_utils import contribute_to_campaign, get_contributions, get_total_funds
from app.data_store import save_contribution, load_contributions


w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))


st.title("Fundraising Campaign for Affected Areas")

st.sidebar.title("Contribute")
account = st.sidebar.selectbox("Account", w3.eth.accounts)
location = st.sidebar.text_input("Location")
amount = st.sidebar.number_input("Amount in Ether", min_value=0.01)

if st.sidebar.button("Contribute"):
    receipt = contribute_to_campaign(account, location, amount)
    save_contribution(account, location, amount)
    st.sidebar.success(f"Contribution successful! Transaction hash: {receipt.transactionHash.hex()}")

st.header("Campaign Summary")
st.write(f"Total Funds Raised: {get_total_funds()} ETH")

st.header("Contributions by Account")
selected_account = st.selectbox("Select Account", w3.eth.accounts)
contributions = get_contributions(selected_account)

for contribution in contributions:
    st.write(f"Amount: {contribution[0]} Wei, Location: {contribution[1]}")
