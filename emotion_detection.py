import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    obj = {"raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=obj, headers=header)
    formatted_response = json.loads(response.text)
    anger = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    if max(anger, disgust, fear, joy, sadness) is joy:
        dominant_emotion = 'joy'
    elif max(anger, disgust, fear, joy, sadness) is sadness:
        dominant_emotion = 'sadness'
    elif max(anger, disgust, fear, joy, sadness) is fear:
        dominant_emotion = 'fear'
    elif max(anger, disgust, fear, joy, sadness) is disgust:
        dominant_emotion = 'disgust'
    elif max(anger, disgust, fear, joy, sadness) is anger:
        dominant_emotion = 'anger'
    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion,
    }