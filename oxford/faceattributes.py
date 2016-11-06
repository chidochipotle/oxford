# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

class HeadPose(dict):
    def __init__(self, pose={}):
        self["roll"] = pose.get("roll", None)
        self["yaw"] = pose.get("yaw", None)
        self["pitch"] = pose.get("pitch", None)

    @property
    def roll(self):
        return self["roll"]

    @roll.setter
    def roll(self, value):
        self["roll"] = value

    @property
    def yaw(self):
        return self["yaw"]

    @yaw.setter
    def yaw(self, value):
        self["yaw"] = value

    @property
    def pitch(self):
        return self["pitch"]

    @pitch.setter
    def pitch(self, value):
        self["pitch"] = value


class FacialHair(dict):
    def __init__(self, hair = {}):
        self["beard"] = hair.get("beard", None)
        self["moustache"] = hair.get("moustache", None)
        self["sideburns"] = hair.get("sideburns", None)

    @property
    def moustache(self):
        return self["moustache"]

    @moustache.setter
    def moustache(self, value):
        self["moustache"] = value

    @property
    def beard(self):
        return self["beard"]

    @beard.setter
    def beard(self, value):
        self["beard"] = value

    @property
    def sideburns(self):
        return self["sideburns"]

    @sideburns.setter
    def sideburns(self, value):
        self["sideburns"] = value

#TODO: Add glasses enum
#class Glasses(object):
#    NO_GLASSES = 1
#    SUNGLASSES = 2
#    READING_GLASSES = 3
#    SWIMMING_GLASSES = 4


class FaceAttributes(dict):
    def __init__(self, attributes={}):
        self["age"] = attributes.get('age', None)
        self["gender"] = attributes.get('gender', None)
        self["head_pose"] = HeadPose(attributes.get('headPose', {}))
        self["facial_hair"] = FacialHair(attributes.get('facialHair', {}))
        self["smile"] = attributes.get('smile', None)
        self["glasses"] = attributes.get('glasses', None)

    @property
    def age(self):
        return self["age"]

    @age.setter
    def age(self, value):
        self["age"] = value

    @property
    def gender(self):
        return self["gender"]

    @gender.setter
    def gender(self, value):
        self["gender"] = value

    @property
    def head_pose(self):
        return self["head_pose"]

    @head_pose.setter
    def head_pose(self, value):
        self["head_pose"] = value

    @property
    def smile(self):
        return self["smile"]

    @smile.setter
    def smile(self, value):
        self["smile"] = value

    @property
    def facial_har(self):
        return self["facial_har"]

    @facial_har.setter
    def facial_har(self, value):
        self["facial_har"] = value

    @property
    def glasses(self):
        return self["glasses"]

    @glasses.setter
    def glasses(self, value):
        self["glasses"] = value
