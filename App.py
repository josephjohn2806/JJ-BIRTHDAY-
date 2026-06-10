tfrom flask import Flask, jsonify

app = Flask(__name__)

@app.route('/explore', methods=['POST'])
def process_exploration_request():
    print("Action Button clicked: Routing traveler to packages asset index...")
    return jsonify({
        "status": "success",
        "redirect_target": "packages_index",
        "message": "Welcome to Musembi Earthways Safaris"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/explore', methods=['POST'])
def process_main_explore():
    return jsonify({"status": "success", "msg": "Navigating from Main landing page"})

@app.route('/package-inquiry', methods=['POST'])
def process_package_inquiry():
    print("Inquiry form entry received from package tracking page.")
    return jsonify({"status": "success", "message": "Inquiry successfully recorded!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

