# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

from .facerectangle import FaceRectangle

from collections import OrderedDict

class EmotionModel(OrderedDict):
    def __init__(self, result):
        if result:
            try:
                self["face_rectangle"] = FaceRectangle(result['faceRectangle'])
                self["scores"] = Scores(result['scores'])
            except KeyError:
                raise KeyError("faceID or scores missing in dict" + str(result))

    @property
    def face_id(self):
        print("returning")
        return self["face_id"]

    @face_id.setter
    def face_id(self, value):
        print(("setting", value))
        self["face_id"] = value

class Scores(OrderedDict):

    def __init__(self, scores):
        self.anger = scores.get(scores["anger"], None)
        self.contempt = scores.get(scores["contempt"], None)
        self.disgust = scores.get(scores["disgust"], None)
        self.fear = scores.get(scores["fear"], None)
        self.happiness = scores.get(scores["happiness"], None)
        self.neutral = scores.get(scores["neutral"], None)
        self.sadness = scores.get(scores["sadness"], None)
        self.surprise = scores.get(scores["surprise"], None)

    @property
    def anger(self):
        return self["anger"]

    @anger.setter
    def anger(self, value):
        self["anger"] = value

    @property
    def contempt(self):
        return self["contempt"]

    @contempt.setter
    def contempt(self, value):
        self["contempt"] = value

    @property
    def disgust(self):
        return self["disgust"]

    @disgust.setter
    def disgust(self, value):
        self["disgust"] = value

    @property
    def fear(self):
        return self["fear"]

    @fear.setter
    def fear(self, value):
        self["fear"] = value

    @property
    def happiness(self):
        return self["happiness"]

    @happiness.setter
    def happiness(self, value):
        self["happiness"] = value

    @property
    def neutral(self):
        return self["neutral"]

    @neutral.setter
    def neutral(self, value):
        self["neutral"] = value

    @property
    def sadness(self):
        return self["sadness"]

    @sadness.setter
    def sadness(self, value):
        self["sadness"] = value

    @property
    def surprise(self):
        return self["surprise"]

    @surprise.setter
    def surprise(self, value):
        self["surprise"] = value

    def to_ranked_list(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError

    def get_hash_code(self):
        raise NotImplementedError
