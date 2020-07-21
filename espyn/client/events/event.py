"id": "401220225",
        "uid": "s:20~l:28~e:401220225",
        "date": "2020-09-11T00:20Z",
        "name": "Houston Texans at Kansas City Chiefs",
        "shortName": "HOU @ KC",
        "season": {
            "year": 2020,
            "type": 2
        },


class Event(object):

    def __init__(self, data):
        self.raw = data
        self.uid = self.data.get("uid")
        self.date = self.data.get("date")
        self.long_description = self.get("name")
        self.short_description = self.get("shortName")

    @property
    def season(self):
        return self.raw.get("season")