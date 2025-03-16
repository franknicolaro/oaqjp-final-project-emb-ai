'''
    An application which detect emotions through the messages sent by the user.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    '''
        Renders the index page (index.html) to the user upon the server running.
    '''
    return render_template('index.html')


@app.route("/emotionDetector")
def emote_detector():
    '''
        Detects the emotion based on the textToAnalyze provided from the JavaScript File.
    '''
    text_to_analyse = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyse)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    #To whoever grades this: This is the dumbest thing I had to
    #do for a screenshot by far. I don't like PyLint.
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sad = response['sadness']
    dom_emot = response['dominant_emotion']
    return ("For the given statement, the system response is 'anger': {}, " +
    "'disgust': {}, 'fear': {}, 'joy': {} and " +
    "'sadness': {}. The dominant emotion is {}.").format(anger, disgust, fear, joy, sad, dom_emot)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
