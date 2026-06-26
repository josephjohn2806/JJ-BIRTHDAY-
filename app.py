from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

wishes_db = [
    {"name": "Amara", "text": "Wishing you unparalleled success this year, JJ!"}
]

@app.route('/api/wishes', methods=['GET', 'POST'])
def handle_wishes():
    if request.method == 'POST':
        data = request.get_json()
        wishes_db.insert(0, {"name": data['name'], "text": data['text']})
        return jsonify({"status": "Success"}), 201
    return jsonify(wishes_db)

@app.route('/api/gift/mpesa', methods=['POST'])
def trigger_stk_push():
    data = request.get_json()
    phone = data.get('phone')
    amount = data.get('amount')
    
    # Placeholder parameters matching the Safaricom Daraja API Framework
    # Real implementations construct authentication tokens here
    print(f"Triggering STK Push to target phone: {phone} for KES {amount}")
    return jsonify({"Status": "STK Push Sent Successfully", "CheckoutRequestID": "ws_CO_26062026"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)

