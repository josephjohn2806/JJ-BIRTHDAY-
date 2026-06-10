from flask import Flask, jsonify

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
