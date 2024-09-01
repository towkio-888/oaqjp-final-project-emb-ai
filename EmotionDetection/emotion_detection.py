# emotion_detection.py
import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank input
    if not text_to_analyze.strip():
        # Return a dictionary with all values as None for blank input
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    # Define the URL and headers for the Watson Emotion API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    
    # Define the input JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Make the POST request to the API
    response = requests.post(url, headers=headers, json=payload)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to a dictionary
        response_dict = response.json()

        # Extract emotions and their scores
        emotions = response_dict.get('emotion', {})
        anger_score = emotions.get('anger', 0)
        disgust_score = emotions.get('disgust', 0)
        fear_score = emotions.get('fear', 0)
        joy_score = emotions.get('joy', 0)
        sadness_score = emotions.get('sadness', 0)
        
        # Create a dictionary of the required emotions and their scores
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        
        # Add the dominant emotion to the output dictionary
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        # Return the output in the required format
        return emotion_scores

    elif response.status_code == 400:
        # Handle errors for bad requests by returning a dictionary with all values as None
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    else:
        # Handle other errors and return the error message
        error_message = f"API request failed with status code {response.status_code}: {response.text}"
        return {"error": error_message}
