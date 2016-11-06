# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

import copy
import os
import sys
import unittest

rootDirectory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if rootDirectory not in sys.path:
    sys.path.insert(0, rootDirectory)

from oxford.emotion import Emotion
from oxford.emotionmodel import EmotionModel

class TestEmotionModel(unittest.TestCase):
    '''Tests the project oxford EmotionModel API self.client'''

    @classmethod
    def setUpClass(cls):
        # set up self.client for tests
        cls.client = Emotion(os.environ['OXFORD_EMOTION_API_KEY'])

        cls.localFilePrefix = os.path.join(rootDirectory, 'tests', 'images')

        # set common recognize options
        cls.recognizeOptions = {
            'faceRectangles': ''
        }

    #
    # test the recognize API
    #
    def _verifyRecognize(self, recognizeResult):
        for emotionResult in recognizeResult:
            emotion_model = EmotionModel(emotionResult)
            self.assertIsInstance(emotion_model['face_rectangle'], object, 'face rectangle is returned')
            scores = emotion_model['scores']
            self.assertIsInstance(scores, object, 'scores are returned')

    def test_emotion_recognize_file(self):
        options = copy.copy(self.recognizeOptions)
        options['path'] = os.path.join(self.localFilePrefix, 'face1.jpg')
        recognizeResult = self.client.recognize(options)
        self._verifyRecognize(recognizeResult)
