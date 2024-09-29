from web3 import Web3
from solcx import compile_source, install_solc, set_solc_version

# Install Solidity compiler
install_solc('0.8.27')

# Set the compiler version to the one we just installed
set_solc_version('0.8.27')

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Load and compile contract
with open('blockchain/contract.sol', 'r') as file:
    contract_source_code = file.read()

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:FundraisingCampaign']

# Deploy the contract
FundraisingCampaign = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get the default account (this should be the owner)
w3.eth.default_account = w3.eth.accounts[0]

# Deploy the contract
tx_hash = FundraisingCampaign.constructor().transact({'gas': 4500000})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"Contract deployed at address: {contract_address}")

# Save the contract address and ABI
with open('app/contract_info.py', 'w') as f:
    f.write(f"contract_address = '{contract_address}'\n")
    f.write(f"contract_abi = {contract_interface['abi']}\n")
