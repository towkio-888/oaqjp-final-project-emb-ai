# test_emotion_detection.py
import unittest
from emotion_detection import emotion_detector
import json

class TestEmotionDetector(unittest.TestCase):
    def assertDominantEmotion(self, text, expected_emotion):
        result = emotion_detector(text)
        result_dict = json.loads(result)
        # Debug output to see what the API is actually returning
        print(f"Testing text: {text}")
        print(f"API Response: {result_dict}")

        # Check if the dominant emotion matches the expected value
        self.assertEqual(result_dict.get('dominant_emotion'), expected_emotion,
                         f"Expected dominant emotion '{expected_emotion}' but got '{result_dict.get('dominant_emotion')}'")

    def test_joy(self):
        self.assertDominantEmotion("I am glad this happened", "joy")

    def test_anger(self):
        self.assertDominantEmotion("I am really mad about this", "anger")

    def test_disgust(self):
        self.assertDominantEmotion("I feel disgusted just hearing about this", "disgust")

    def test_sadness(self):
        self.assertDominantEmotion("I am so sad about this", "sadness")

    def test_fear(self):
        self.assertDominantEmotion("I am really afraid that this will happen", "fear")

unittest.main()
