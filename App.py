from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/inquire', methods=['POST'])
def handling_safari_inquiry():
    # Logs inquiries directly on the server
    print("Inquiry incoming for Musembi Earthways Safaris packages!")
    
    # Ready to be linked to a structured client confirmation email system
    return """
    <html>
        <body style="font-family:sans-serif; text-align:center; padding-top:100px; background-color:#fcfaf7; color:#1b4332;">
            <h2>Asante Sana!</h2>
            <p>Your safari interest has rolled in. An Earthways specialist will reach out shortly.</p>
            <br>
            <a href="http://127.0.0.1:5500/index.html" style="color:#40916c; text-decoration:none; font-weight:bold;">← Return to Journeys</a>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5000)

