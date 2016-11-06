# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

from collections import OrderedDict


class AnalysisResults(OrderedDict):
    def __init__(self, result):
        if result:
            try:
                self["request_id"] = result.get("requestId", None)
                self["metadata"] = Metadata(result.get("metadata", {}))
                self["image_type"] = ImageType(result.get("imageType", {}))
                self["color"] = Color(result.get("color", {}))
                self["adult"] = Adult(result.get("adult", {}))
                self["categories"] = Categories(result.get("categories", {}))
                self["faces"] = Faces(result.get("faces", {}))
                self["tags"] = Tags(result.get("tags", {}))
                self["description"] = Description(result.get("description", {}))
            except KeyError:
                raise KeyError("requestId missing in dict" + str(result))

    @property
    def request_id(self):
        return self["request_id"]

    @request_id.setter
    def request_id(self, value):
        self["request_id"] = value

    @property
    def metadata(self):
        return self["metadata"]

    @metadata.setter
    def metadata(self, value):
        self["metadata"] = value

    @property
    def image_type(self):
        return self["image_type"]

    @image_type.setter
    def image_type(self, value):
        self["image_type"] = value

    @property
    def color(self):
        return self["color"]

    @color.setter
    def color(self, value):
        self["color"] = value

    @property
    def adult(self):
        return self["adult"]

    @adult.setter
    def adult(self, value):
        self["adult"] = value

    @property
    def categories(self):
        return self["categories"]

    @categories.setter
    def categories(self, value):
        self["categories"] = value

    @property
    def faces(self):
        return self["faces"]

    @faces.setter
    def faces(self, value):
        self["faces"] = value

    @property
    def tags(self):
        return self["tags"]

    @tags.setter
    def tags(self, value):
        self["tags"] = value

    @property
    def description(self):
        return self["description"]

    @description.setter
    def description(self, value):
        self["description"] = value


class Metadata(OrderedDict):

    def __init__(self, metadata={}):
        self["width"] = metadata.get("width", None)
        self["height"] = metadata.get("height", None)
        self["format"] = metadata.get("format", None)

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
    def format(self):
        return self["format"]

    @format.setter
    def format(self, value):
        self["format"] = value


class ImageType(OrderedDict):

    def __init__(self, image_type={}):
        self["clip_art_type"] = image_type.get("clipArtType", None)
        self["line_drawing_type"] = image_type.get("lineDrawingType", None)

    @property
    def clip_art_type(self):
        return self["clip_art_type"]

    @clip_art_type.setter
    def clip_art_type(self, value):
        self["clip_art_type"] = value

    @property
    def line_drawing_type(self):
        return self["line_drawing_type"]

    @line_drawing_type.setter
    def line_drawing_type(self, value):
        self["line_drawing_type"] = value


class Color(OrderedDict):

    def __init__(self, color={}):
        self["accent_color"] = color.get("accentColor", None)
        self["dominant_color_foreground"] = color.get("dominantColorForeground", None)
        self["dominant_color_background"] = color.get("dominantColorBackground", None)
        self["dominant_colors"] = color.get("dominantColors", None)
        self["is_bw_img"] = color.get("isBWImg", None)

    @property
    def accent_color(self):
        return self["accent_color"]

    @accent_color.setter
    def accent_color(self, value):
        self["accent_color"] = value

    @property
    def dominant_color_foreground(self):
        return self["dominant_color_foreground"]

    @dominant_color_foreground.setter
    def dominant_color_foreground(self, value):
        self["dominant_color_foreground"] = value

    @property
    def dominant_color_background(self):
        return self["dominant_color_background"]

    @dominant_color_background.setter
    def dominant_color_background(self, value):
        self["dominant_color_background"] = value

    @property
    def dominant_colors(self):
        return self["dominant_colors"]

    @dominant_colors.setter
    def dominant_colors(self, value):
        self["dominant_colors"] = value

    @property
    def is_bw_img(self):
        return self["is_bw_img"]

    @is_bw_img.setter
    def is_bw_img(self, value):
        self["is_bw_img"] = value


class Adult(OrderedDict):

    def __init__(self, adult={}):
        self["is_adult_content"] = adult.get("isAdultContent", None)
        self["is_racy_content"] = adult.get("isRacyContent", None)
        self["adult_score"] = adult.get("adultScore", None)
        self["racy_score"] = adult.get("racyScore", None)

    @property
    def is_adult_content(self):
        return self["is_adult_content"]

    @is_adult_content.setter
    def is_adult_content(self, value):
        self["is_adult_content"] = value

    @property
    def is_racy_content(self):
        return self["is_racy_content"]

    @is_racy_content.setter
    def is_racy_content(self, value):
        self["is_racy_content"] = value

    @property
    def adult_score(self):
        return self["adult_score"]

    @adult_score.setter
    def adult_score(self, value):
        self["adult_score"] = value

    @property
    def racy_score(self):
        return self["racy_score"]

    @racy_score.setter
    def racy_score(self, value):
        self["racy_score"] = value


class Rectangle(dict):

    def __init__(self, rectangle={}):
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


class Face(OrderedDict):

    def __init__(self, face={}):
        self["age"] = face.get("age", None)
        self["gender"] = face.get("gender", None)
        self["face_rectangle"] = Rectangle(face['faceRectangle'])

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
    def face_rectangle(self):
        return self["face_rectangle"]

    @face_rectangle.setter
    def face_rectangle(self, value):
        self["face_rectangle"] = value


class Faces(list):

    def __init__(self, faces=[]):
        for face in faces:
            self.append(face)


class Tag(OrderedDict):

    def __init__(self, tag={}):
        self["name"] = tag.get("name", None)
        self["confidence"] = tag.get("confidence", None)
        self["hint"] = tag.get("hint", None)

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, value):
        self["name"] = value

    @property
    def confidence(self):
        return self["confidence"]

    @confidence.setter
    def confidence(self, value):
        self["confidence"] = value

    @property
    def hint(self):
        return self["hint"]

    @hint.setter
    def hint(self, value):
        self["hint"] = value


class Tags(list):

    def __init__(self, tags=[]):
        for tag in tags:
            self.append(tag)


class Captions(list):

    def __init__(self, captions=[]):
        for caption in captions:
            self.append(caption)


class Caption(OrderedDict):

    def __init__(self, description={}):
        self["text"] = description.get(description.get("text", []), None)
        self["confidence"] = description.get(description.get("confidence", []), None)

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, value):
        self["text"] = value

    @property
    def confidence(self):
        return self["confidence"]

    @confidence.setter
    def confidence(self, value):
        self["confidence"] = value


class Description(OrderedDict):

    def __init__(self, description={}):
        self["tags"] = Tags(description.get("tags", []))
        self["captions"] = Captions(description.get("captions", []))

    @property
    def tags(self):
        return self["tags"]

    @tags.setter
    def tags(self, value):
        self["tags"] = value

    @property
    def captions(self):
        return self["captions"]

    @captions.setter
    def captions(self, value):
        self["captions"] = value


class NameScorePair(OrderedDict):
    def __init__(self, name_score_pair={}):
        self["name"] = name_score_pair.get("name", None)
        self["score"] = name_score_pair.get("score", None)

    @property
    def name(self):
        return self["name"]

    @name.setter
    def name(self, value):
        self["name"] = value

    @property
    def score(self):
        return self["score"]

    @score.setter
    def score(self, value):
        self["score"] = value


class Category(NameScorePair):

    def __init__(self, description={}):
        self["detail"] = description.get(description.get("detail", None))

    @property
    def text(self):
        return self["text"]

    @text.setter
    def text(self, value):
        self["text"] = value


# In all list extract ???
class Categories(list):
    def __init__(self, categories=[]):
        for category in categories:
            self.append(category)
