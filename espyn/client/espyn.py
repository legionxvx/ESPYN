from urllib.parse import urljoin

from requests import Session


class ESPYN(Session):

    def __init__(self, sport=None):
        super().__init__()
        self._sport = sport

    @property
    def sport(self):
        return self._sport

    @sport.setter
    def sport(self, value):
        self._sport = value
        return self._sport

    @staticmethod
    def multijoin(url, *parts, seperator="/"):
        return urljoin(url, seperator.join(parts)) + "/"

    @property
    def prefix(self):
        return self.multijoin(
            # Hardcoded for now
            "https://site.api.espn.com/apis/site/v2/sports/",
            self.sport.name,
            self.sport.league.name
        )

    def request(self, method, suffix, *args, **kwargs):
        url = urljoin(self.prefix, suffix)
        return super().request(method, url, *args, **kwargs)

    def get_scoreboard(self, *args, **kwargs):
        kwargs["seasontype"] = kwargs.get(
            "seasontype", 
            self.sport.league.season
        )
        return self.get("scoreboard", *args, **kwargs)