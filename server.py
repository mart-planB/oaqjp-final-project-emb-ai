"""
Flask server for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

# Route for the emotion detection function
@app.route("/emotionDetector")
def emotion_detector_function():
    """
    Emotion Dectection Code
    """
    # Get the text input from the GET request
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function with the text input
    response = emotion_detector(text_to_analyze)

    # Extract the individual emotion scores and dominant emotion
    emotions = response
    dominant_emotion = response['dominant_emotion']

    # Handle cases where dominant_emotion is None (invalid text)
    if dominant_emotion is None:
        return "Invalid text! Please try again."

    # Format and return the response using an f-string
    return (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, 'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. The dominant emotion is {dominant_emotion}."
    )

# Route to render the index.html page
@app.route("/")
def render_index_page():
    """
    Route to index.html page.
    """
    return render_template('index.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
