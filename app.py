from flask import Flask, request, render_template
from web3_connect import contract, web3
import hashlib

app = Flask(__name__)

def get_document_hash(file):
    file_content = file.read()
    return hashlib.sha256(file_content).hexdigest()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        file = request.files["document"]
        doc_hash = get_document_hash(file)

        # Check if hash is already on blockchain
        is_registered = contract.functions.verifyDocument(bytes.fromhex(doc_hash)).call()
        
        if request.form["action"] == "register":
            if not is_registered:
                tx_hash = contract.functions.registerDocument(bytes.fromhex(doc_hash)).transact()
                web3.eth.wait_for_transaction_receipt(tx_hash)
                message = "✅ Document registered successfully!"
            else:
                message = "⚠️ Document already registered!"
        
        elif request.form["action"] == "verify":
            message = "✅ Document is authentic!" if is_registered else "❌ Document not found!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
