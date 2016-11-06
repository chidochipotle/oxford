# Copyright (c) 2016 Daniel Kornhauser under The MIT License (MIT)

from .featurecoordinate import FeatureCoordinate


class FaceLandmarks(dict):

    def __init__(self, features={}):
        self['eyeLeftInner'] = FeatureCoordinate(features.get('eyeLeftInner', {}))
        self['eyeLeftOuter'] = FeatureCoordinate(features.get('eyeLeftOuter', {}))
        self['eyeLeftTop'] = FeatureCoordinate(features.get('eyeLeftTop', {}))
        self['eyeRightBottom'] = FeatureCoordinate(features.get('eyeRightBottom', {}))
        self['eyeRightInner'] = FeatureCoordinate(features.get('eyeRightInner', {}))
        self['eyeRightOuter'] = FeatureCoordinate(features.get('eyeRightOuter', {}))
        self['eyeRightTop'] = FeatureCoordinate(features.get('eyeRightTop', {}))
        self['eyebrowLeftInner'] = FeatureCoordinate(features.get('eyebrowLeftInner', {}))
        self['eyebrowLeftOuter'] = FeatureCoordinate(features.get('eyebrowLeftOuter', {}))
        self['eyebrowRightInner'] = FeatureCoordinate(features.get('eyebrowRightInner', {}))
        self['eyebrowRightOuter'] = FeatureCoordinate(features.get('eyebrowRightOuter', {}))
        self['mouthLeft'] = FeatureCoordinate(features.get('mouthLeft', {}))
        self['mouthRight'] = FeatureCoordinate(features.get('mouthRight', {}))
        self['noseLeftAlarOutTip'] = FeatureCoordinate(features.get('noseLeftAlarOutTip', {}))
        self['noseLeftAlarTop'] = FeatureCoordinate(features.get('noseLeftAlarTop', {}))
        self['noseRightAlarOutTip'] = FeatureCoordinate(features.get('noseRightAlarOutTip', {}))
        self['noseRightAlarTop'] = FeatureCoordinate(features.get('noseRightAlarTop', {}))
        self['noseRootLeft'] = FeatureCoordinate(features.get('noseRootLeft', {}))
        self['noseRootRight'] = FeatureCoordinate(features.get('noseRootRight', {}))
        self['noseTip'] = FeatureCoordinate(features.get('noseTip', {}))
        self['pupilLeft'] = FeatureCoordinate(features.get('pupilLeft', {}))
        self['pupilRight'] = FeatureCoordinate(features.get('pupilRight', {}))
        self['underLipBottom'] = FeatureCoordinate(features.get('underLipBottom', {}))
        self['underLipTop'] = FeatureCoordinate(features.get('underLipTop', {}))
        self['upperLipBottom'] = FeatureCoordinate(features.get('upperLipBottom', {}))
        self['upperLipTop'] = FeatureCoordinate(features.get('upperLipTop', {}))

    @property
    def pupil_left(self):
        return self["pupil_left"]

    @pupil_left.setter
    def pupil_left(self, value):
        self["pupil_left"] = value

    @property
    def pupil_right(self):
        return self["pupil_right"]

    @pupil_right.setter
    def pupil_right(self, value):
        self["pupil_right"] = value

    @property
    def nose_tip(self):
        return self["nose_tip"]

    @nose_tip.setter
    def nose_tip(self, value):
        self["nose_tip"] = value

    @property
    def mouth_right(self):
        return self["mouth_right"]

    @mouth_right.setter
    def mouth_right(self, value):
        self["mouth_right"] = value

    @property
    def eyebrow_left_outer(self):
        return self["eyebrow_left_outer"]

    @eyebrow_left_outer.setter
    def eyebrow_left_outer(self, value):
        self["eyebrow_left_outer"] = value

    @property
    def eyebrow_left_inner(self):
        return self["eyebrow_left_inner"]

    @eyebrow_left_inner.setter
    def eyebrow_left_inner(self, value):
        self["eyebrow_left_inner"] = value

    @property
    def eye_left_outer(self):
        return self["eye_left_outer"]

    @eye_left_outer.setter
    def eye_left_outer(self, value):
        self["eye_left_outer"] = value

    @property
    def eye_left_top(self):
        return self["eye_left_top"]

    @eye_left_top.setter
    def eye_left_top(self, value):
        self["eye_left_top"] = value

    @property
    def eye_left_bottom(self):
        return self["eye_left_bottom"]

    @eye_left_bottom.setter
    def eye_left_bottom(self, value):
        self["eye_left_bottom"] = value

    @property
    def eye_left_inner(self):
        return self["eye_left_inner"]

    @eye_left_inner.setter
    def eye_left_inner(self, value):
        self["eye_left_inner"] = value

    @property
    def eyebrow_right_outer(self):
        return self["eyebrow_right_outer"]

    @eyebrow_right_outer.setter
    def eyebrow_right_outer(self, value):
        self["eyebrow_right_outer"] = value

    @property
    def eyebrow_right_inner(self):
        return self["eyebrow_right_inner"]

    @eyebrow_right_inner.setter
    def eyebrow_right_inner(self, value):
        self["eyebrow_right_inner"] = value

    @property
    def eye_right_outer(self):
        return self["eye_right_outer"]

    @eye_right_outer.setter
    def eye_right_outer(self, value):
        self["eye_right_outer"] = value

    @property
    def eye_right_top(self):
        return self["eye_right_top"]

    @eye_right_top.setter
    def eye_right_top(self, value):
        self["eye_right_top"] = value

    @property
    def eye_right_bottom(self):
        return self["eye_right_bottom"]

    @eye_right_bottom.setter
    def eye_right_bottom(self, value):
        self["eye_right_bottom"] = value

    @property
    def eye_right_inner(self):
        return self["eye_right_inner"]

    @eye_right_inner.setter
    def eye_right_inner(self, value):
        self["eye_right_inner"] = value

    @property
    def nose_root_left(self):
        return self["nose_root_left"]

    @nose_root_left.setter
    def nose_root_left(self, value):
        self["nose_root_left"] = value

    @property
    def nose_root_right(self):
        return self["nose_root_right"]

    @nose_root_right.setter
    def nose_root_right(self, value):
        self["nose_root_right"] = value

    @property
    def nose_left_alar_top(self):
        return self["nose_left_alar_top"]

    @nose_left_alar_top.setter
    def nose_left_alar_top(self, value):
        self["nose_left_alar_top"] = value

    @property
    def nose_right_alar_top(self):
        return self["nose_right_alar_top"]

    @nose_right_alar_top.setter
    def nose_right_alar_top(self, value):
        self["nose_right_alar_top"] = value

    @property
    def nose_left_alar_out_tip(self):
        return self["nose_left_alar_out_tip"]

    @nose_left_alar_out_tip.setter
    def nose_left_alar_out_tip(self, value):
        self["nose_left_alar_out_tip"] = value

    @property
    def nose_right_alar_out_tip(self):
        return self["nose_right_alar_out_tip"]

    @nose_right_alar_out_tip.setter
    def nose_right_alar_out_tip(self, value):
        self["nose_right_alar_out_tip"] = value

    @property
    def upper_lip_top(self):
        return self["upper_lip_top"]

    @upper_lip_top.setter
    def upper_lip_top(self, value):
        self["upper_lip_top"] = value

    @property
    def upper_lip_bottom(self):
        return self["upper_lip_bottom"]

    @upper_lip_bottom.setter
    def upper_lip_bottom(self, value):
        self["upper_lip_bottom"] = value

    @property
    def under_lip_top(self):
        return self["under_lip_top"]

    @under_lip_top.setter
    def under_lip_top(self, value):
        self["under_lip_top"] = value

    @property
    def under_tip_bottom(self):
        return self["under_tip_bottom"]

    @under_tip_bottom.setter
    def under_tip_bottom(self, value):
        self["under_tip_bottom"] = value
