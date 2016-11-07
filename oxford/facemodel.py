# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

from .facelandmarks import FaceLandmarks
from .facerectangle import FaceRectangle
from .faceattributes import FaceAttributes

from collections import OrderedDict

import traceback

class FaceModel(OrderedDict):
    def __init__(self, result):
        super(FaceModel, self).__init__()
        if result:
            try:
                self["face_id"] = result['faceId']
                self["face_rectangle"] = FaceRectangle(result['faceRectangle'])
            except KeyError:
                raise KeyError("faceID or faceRectangle missing in dict" + str(result))

        elif result == {}:
            self["face_id"] = None
            self["face_rectangle"] = FaceRectangle()
        else:
            raise ValueError("Invalid constructor argument", result)
        self["face_landmarks"] = FaceLandmarks(result['faceLandmarks'])
        self["face_attributes"] = FaceAttributes(result['faceAttributes'])

    def load_dict(self, result):
        self["face_id"] = result['faceId']
        self["face_rectangle"] = FaceRectangle(result['faceRectangle'])
        if hasattr(result, 'face_landmarks'):
            FaceLandmarks(result['face_landmarks'])
        if hasattr(result, 'face_attributes'):
            FaceAttributes(result['face_attributes'])

    def load_json(self, result):
        pass

    @property
    def face_id(self):
        print("returning")
        return self["face_id"]

    @face_id.setter
    def face_id(self, value):
        print(("setting", value))
        self["face_id"] = value

    @property
    def face_landmarks(self):
        return self["face_landmarks"]

    @face_landmarks.setter
    def face_landmarks(self, value):
        self["face_landmarks"] = value

    @property
    def face_rectangle(self):
        return self["face_rectangle"]

    @face_rectangle.setter
    def face_rectangle(self, value):
        self["face_rectangle"] = value

    @property
    def face_attributes(self):
        return self["face_attributes"]

    @face_attributes.setter
    def face_attributes(self, value):
        self["face_attributes"] = value
