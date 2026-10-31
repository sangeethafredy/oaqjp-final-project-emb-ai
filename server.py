""" Flask application to detect emotions in user provided text."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app=Flask(__name__)

@app.route('/emotionDetector')
def emotion_detector_route():
    """ Analyze the submitted text and return its emotion scores."""

    text_to_analyze= request.args.get("textToAnalyze")
    response= emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Inavalid response! Please Try again!"
    anger= response['anger']
    disgust= response['disgust']
    fear= response['fear']
    joy= response['joy']
    sadness= response['sadness']
    dominant_emotion= response['dominant_emotion']
    formatted_response=(
        f"For the given statement, the system response is"
        f"'anger': {anger}, 'disgust': {disgust}," 
        f"'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}."
        f"The dominant emotion is {dominant_emotion}"
    )
    return formatted_response

@app.route("/")
def render_index_page():
    """ Render the application's home page"""
    return render_template('index.html')

if __name__== "__main__":
    app.run(host='0.0.0.0', port=5000)
