from enum import IntEnum, auto

class CFBSeasonType(IntEnum):
    REGULAR = 2
    BOWLS = 3

class CFB(object):

    def __init__(self):
        self.name = "college-football"
        self.season = CFBSeasonType.REGULAR