
"""Flask web application for the IBM Emotion Detector."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

# Create the Flask application.
app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_analyzer():
    """Analyze submitted text and return its emotion scores."""

    # Retrieve the text and handle missing or blank input.
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return "Error: Please enter text to analyze.", 400

    # Run the emotion detection service.
    response = emotion_detector(text_to_analyze)

    # Handle unsuccessful emotion detection.
    if not response or response.get("dominant_emotion") is None:
        return "Error: Unable to analyze the text. Please try again.", 400

    # Return the emotion scores and dominant emotion.
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """Render the application's home page."""

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
