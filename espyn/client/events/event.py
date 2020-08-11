class Event(object):

    def __init__(self, data):
        self.raw = data
        self.id = self.data.get("id")
        self.uid = self.data.get("uid")
        self.date = self.data.get("date")
        self.long_description = self.get("name")
        self.short_description = self.get("shortName")

    @property
    def season(self):
        return self.raw.get("season")

class FootballGame(Event):
    def __init__(self, data):
        super().__init__(data)
