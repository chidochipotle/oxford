# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

import copy
import os
import sys
import time
import unittest


rootDirectory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
if rootDirectory not in sys.path:
    sys.path.insert(0, rootDirectory)

from oxford.face import Face
from oxford.facemodel import FaceModel
from oxford.emotionmodel import EmotionModel

class TestFaceModel(unittest.TestCase):
    '''Tests the Project Oxford FaceModel API'''

    @classmethod
    def setUpClass(cls):
        # set up self.client for tests
        cls.client = Face(os.environ['OXFORD_FACE_API_KEY'])

        # detect two faces
        cls.knownFaceIds = [];
        cls.localFilePrefix = os.path.join(rootDirectory, 'tests', 'images')
        face1 = cls.client.detect({'path': os.path.join(cls.localFilePrefix, 'face1.jpg')})
        face2 = cls.client.detect({'path': os.path.join(cls.localFilePrefix, 'face2.jpg')})
        cls.knownFaceIds.append(face1[0]['faceId'])
        cls.knownFaceIds.append(face2[0]['faceId'])

        # set common detect options
        cls.detectOptions = {
            'returnFaceLandmarks': True,
            'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses'
        }
        

    #
    # test the face model API
    #
    def _verifyDetect(self, detectResult):
        faceIdResult = detectResult[0]

        face_model = FaceModel(faceIdResult)

        self.assertIsInstance(face_model['face_id'], object, 'face ID is returned')
        self.assertIsInstance(face_model['face_rectangle'], object, 'faceRectangle is returned')
        self.assertIsInstance(face_model['face_landmarks'], object, 'faceLandmarks are returned')
        
        face_attributes = face_model['face_attributes']
        self.assertIsInstance(face_attributes, object, 'attributes are returned')
        self.assertIsInstance(face_attributes['gender'], object, 'gender is returned')
        self.assertIsInstance(face_attributes.age, float, 'age is returned')

    def test_face_detect_file(self):
        options = copy.copy(self.detectOptions)
        options['path'] = os.path.join(self.localFilePrefix, 'face1.jpg')
        detectResult = self.client.detect(options)
        self._verifyDetect(detectResult)

    @classmethod
    def TearDownUpClass(cls):
        time.sleep(0.5)  # sleep time in seconds
