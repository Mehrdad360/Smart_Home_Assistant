

from flask import Flask, request, jsonify
from flask_cors import CORS  # To handle Cross-Origin Resource Sharing
import os
import sys

# Add the project directory to sys.path to allow imports from other files
# This is crucial when running Flask from a different directory or setup
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import the main assistant logic
from assistant import chat_with_assistant

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes, allowing frontend to access from a different origin


@app.route('/chat', methods=['POST'])
def chat():
    """
    API endpoint for handling chat messages from the frontend.
    Receives a JSON payload with a 'message' key.
    """
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "Missing 'message' in request"}), 400

    print(f"Received message from UI: {user_message}")

    # Process the message with the smart home assistant
    assistant_response = chat_with_assistant(user_message)

    print(f"Sending response to UI: {assistant_response}")
    return jsonify({"response": assistant_response})


@app.route('/')
def home():
    """Basic home route to confirm API is running."""
    return "Smart Home Assistant Backend is running!"


if __name__ == '__main__':
    # When running the Flask app, it also initializes our assistant and devices
    print("Starting Smart Home Assistant Backend...")
    app.run(debug=True, port=5000)  # Run on port 5000, debug=True for development