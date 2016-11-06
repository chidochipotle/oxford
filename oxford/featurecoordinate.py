# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

class FeatureCoordinate(dict):
    def __init__(self, coordinate={}):
        self["x"] = coordinate.get("x", None)
        self["y"] = coordinate.get("y", None)

    @property
    def x(self):
        return self["x"]

    @x.setter
    def x(self, value):
        self["x"] = value

    @property
    def y(self):
        return self["y"]

    @y.setter
    def y(self, value):
        self["y"] = value
