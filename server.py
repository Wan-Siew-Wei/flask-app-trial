from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Railway Flask API is running!"

@app.route("/api/customer/<customer_id>", methods=["GET"])
def get_customer_details(customer_id):
    """Simulate fetching customer loan details based on the provided data"""
    data = {
        "101": {
            "name": "Siti Rohayani",
            "IC_number": "971010019786",
            "Loan_Amount": "RM65,000",
            "Dapat_Dalam_Tangan": "RM48,700",
            "Bayaran_Bulanan": "RM628",
            "Tempoh": "8 bulan",
            "Kos_Pembiayaan": "RM5,000",
            "Pendahuluan_Pembiayaan": "RM9,200",
            "Penyelesaian_Awal": "RM4,000",
            "Baki_Pembiayaan": "RM7,048",
            "address": "Puan"
        },
        "102": {
            "name": "Ahmad Firdaus",
            "IC_number": "890512035678",
            "Loan_Amount": "RM50,000",
            "Dapat_Dalam_Tangan": "RM38,500",
            "Bayaran_Bulanan": "RM750",
            "Tempoh": "10 bulan",
            "Kos_Pembiayaan": "RM4,500",
            "Pendahuluan_Pembiayaan": "RM8,000",
            "Penyelesaian_Awal": "RM3,500",
            "Baki_Pembiayaan": "RM5,200",
            "address": "Encik"
        }
    }
    return jsonify(data.get(customer_id, {"error": "Customer not found"}))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
