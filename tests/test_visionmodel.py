# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)


import copy
import os
import sys
import unittest

rootDirectory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if rootDirectory not in sys.path:
    sys.path.insert(0, rootDirectory)

from oxford.vision import Vision
from oxford.visionmodel import AnalysisResults

class TestFace(unittest.TestCase):
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
    def _verify_analyze_result(self, result):
        analisys_results = AnalysisResults(result)
        self.assertIsNotNone(analisys_results['image_type'])
        self.assertIsNotNone(analisys_results.image_type)
        self.assertIsNotNone(analisys_results['image_type']['clip_art_type'])
        self.assertIsNotNone(analisys_results.image_type.clip_art_type)
        self.assertIsNotNone(analisys_results['color'])
        self.assertIsNotNone(analisys_results['faces'])
        self.assertIsNotNone(analisys_results['adult'])
        self.assertIsNotNone(analisys_results['categories'])

    def test_vision_analyze_file(self):
        options = copy.copy(self.analyzeOptions)
        options['path'] = os.path.join(self.localFilePrefix, 'vision.jpg')
        result = self.client.analyze(options)
        self._verify_analyze_result(result)
