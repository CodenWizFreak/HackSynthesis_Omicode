from web3 import Web3
from app.contract_info import contract_address, contract_abi

# Initialize Web3 connection
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def contribute_to_campaign(account, location, amount):
    tx_hash = contract.functions.contribute(location).transact({'from': account, 'value': w3.toWei(amount, 'ether')})
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt

def get_contributions(account):
    return contract.functions.getContributions(account).call()

def get_total_funds():
    return w3.fromWei(contract.functions.totalFunds().call(), 'ether')
