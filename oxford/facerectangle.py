# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)


class FaceRectangle(dict):

    def __init__(self, rectangle={}):
        super(FaceRectangle, self).__init__()
        self["width"] = rectangle.get("width", None)
        self["height"] = rectangle.get("height", None)
        self["left"] = rectangle.get("left", None)
        self["top"] = rectangle.get("top", None)

    @property
    def width(self):
        return self["width"]

    @width.setter
    def width(self, value):
        self["width"] = value

    @property
    def height(self):
        return self["height"]

    @height.setter
    def height(self, value):
        self["height"] = value

    @property
    def left(self):
        return self["left"]

    @left.setter
    def left(self, value):
        self["left"] = value

    @property
    def top(self):
        return self["top"]

    @top.setter
    def top(self, value):
        self["top"] = value
