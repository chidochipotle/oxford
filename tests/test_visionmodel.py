# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

import copy
import os
import sys
import time
import unittest

rootDirectory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if rootDirectory not in sys.path:
    sys.path.insert(0, rootDirectory)

from oxford.vision import Vision
from oxford.visionmodel import AnalysisResults

class TestVisionModel(unittest.TestCase):
    '''Tests the Project Oxford Vision API'''

    @classmethod
    def setUpClass(cls):
        # set up self.client for tests
        cls.client = Vision(os.environ['OXFORD_VISION_API_KEY'])
        cls.localFilePrefix = os.path.join(rootDirectory, 'tests', 'images')
        cls.analyzeOptions = {
            'ImageType': True,
            'Color': True,
            'Faces': True,
            'Adult': True,
            'Categories': True,
            'Tags': True,
            'Description': True,
            'Celebrities': True,
        }

        cls.thumbnailOptions = {
            'width': 100,
            'height': 100,
            'smartCropping': True
        }

        cls.ocrOptions = {
            'language': 'en',
            'detectOrientation': True
        }

    #
    # test the analyze API
    #
    def _verify_model_analyze_result(self, result):
        analysis_results = AnalysisResults(result)
        self.assertIsNotNone(analysis_results['image_type'])
        self.assertIsNotNone(analysis_results.image_type)
        self.assertIsNotNone(analysis_results['image_type']['clip_art_type'])
        self.assertIsNotNone(analysis_results.image_type.clip_art_type)
        self.assertIsNotNone(analysis_results['color'])
        self.assertIsNotNone(analysis_results['faces'])
        self.assertIsNotNone(analysis_results['adult'])
        self.assertIsNotNone(analysis_results['categories'])

    def test_model_vision_analyze_file(self):
        options = copy.copy(self.analyzeOptions)
        options['path'] = os.path.join(self.localFilePrefix, 'vision.jpg')
        result = self.client.analyze(options)
        self._verify_model_analyze_result(result)


    @classmethod
    def TearDownUpClass(cls):
        time.sleep(0.5)  # sleep time in seconds
