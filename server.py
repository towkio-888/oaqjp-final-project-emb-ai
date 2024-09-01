"""
server.py - Flask application for emotion detection.

This script sets up a Flask web server that detects emotions in text input
using the Watson Emotion API.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the homepage of the Emotion Detector web application.

    Returns:
        str: Rendered HTML template for the homepage.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def detect_emotion():
    """
    Detect the emotion in the text input provided by the user.

    Returns:
        Response: JSON response with emotion scores or an error message.
    """
    text_to_analyze = request.form.get('text')

    if not text_to_analyze or not text_to_analyze.strip():
        # Handle the case where no text is provided
        response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
        return jsonify(response), 400

    # Call the emotion detection function from emotion_detection module
    result = emotion_detector(text_to_analyze)

    if result.get('dominant_emotion') is None:
        # Handle the case where the dominant emotion is None
        response = {
            "error": "Invalid text! Please try again."
        }
        return jsonify(response), 400

    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
