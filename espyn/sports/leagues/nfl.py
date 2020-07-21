from enum import IntEnum, auto

class NFLSeasonType(IntEnum):
    PRESEASON = 1
    REGULAR = 2
    BOWLS = 3

class NFL(object):

    def __init__(self):
        self.name = "nfl"
        self.season = NFLSeasonType.REGULAR