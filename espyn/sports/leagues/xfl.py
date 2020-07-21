from enum import IntEnum, auto

class XFLSeasonType(IntEnum):
    PRESEASON = 1
    REGULAR = 2
    BOWLS = 3

class XFL(object):

    def __init__(self):
        self.name = "xfl"
        self.season = XFLSeasonType.REGULAR