### **📌 Blockchain-Based Document Verification System**  
A blockchain-powered tool that **secures document authenticity** by storing unique document fingerprints (hashes) on a blockchain. Users can verify document integrity by checking if the document’s hash exists on the blockchain.  

---

## **🛠️ Features**  
✔ **Immutable Document Records** – Prevents document tampering.  
✔ **SHA-256 Hashing** – Converts documents into unique, secure hashes.  
✔ **Blockchain Storage** – Stores document hashes on Ethereum blockchain.  
✔ **User-Friendly Interface** – Upload and verify documents easily.  
✔ **Smart Contracts** – Handles document registration and verification.  

---

## **🛠️ Technologies Used**  
| **Technology**  | **Purpose**  |  
|-----------------|-------------|  
| **Python**  | Backend Processing |  
| **Web3.py**  | Blockchain Interaction |  
| **Solidity**  | Smart Contract Development |  
| **Ethereum (Ganache/Testnet)**  | Blockchain Storage |  
| **Flask**  | Web API |  
| **IPFS (InterPlanetary File System)** | Optional: Secure Document Storage |  

---

## **📂 Project Structure**  
```
/Blockchain-Doc-Verify
│── app.py               # Flask API for document verification
│── contract.sol         # Ethereum smart contract
│── requirements.txt     # Dependencies
│── web3_connect.py      # Blockchain connection script
│── templates/
│   ├── index.html       # Web interface
│── static/
│   ├── style.css        # Styling
│── README.md            # Documentation
```


---

### ** Deploy the Smart Contract**  
Use Remix IDE or Hardhat to deploy the contract on Ethereum testnet.  

---


## **🛠️ How to Run the Project**  
1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/prangowda/Blockchain-Doc-Verify.git
cd Blockchain-Doc-Verify
```

2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

3️⃣ **Deploy Smart Contract on Ethereum Testnet** (Use Remix/Hardhat)  
4️⃣ **Update Contract Address & ABI in `web3_connect.py`**  
5️⃣ **Run Flask App**  
```sh
python app.py
```

---

## **🚀 How It Works?**  
✅ **Upload a Document** – Generates a **SHA-256 hash**  
✅ **Register the Document** – Hash is stored on **Ethereum blockchain**  
✅ **Verify the Document** – Checks blockchain for authenticity  

---

## **🔮 Future Enhancements**  
✔ **IPFS Integration** – Securely store document files  
✔ **QR Code Verification** – Verify authenticity via QR scan  
✔ **Mobile App** – React Native/Flutter version  
