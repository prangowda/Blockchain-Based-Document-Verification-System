from web3 import Web3

infura_url = "https://sepolia.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

contract_address = "YOUR_DEPLOYED_CONTRACT_ADDRESS"
abi = [...]  # Paste the ABI from Remix after deployment

contract = web3.eth.contract(address=contract_address, abi=abi)
