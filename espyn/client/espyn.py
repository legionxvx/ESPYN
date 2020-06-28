from urllib.parse import urljoin

from requests import Session


class League(object):
    FOOTBALL = "football"

class Sport(object):
    COLLEGE_FOOTBALL = "college-football"


class ESPYN(Session):

    def __init__(self, league=None, sport=None):
        super().__init__()
        self._league = league
        self._sport = sport

    @property
    def league(self):
        return self._league or ""

    @league.setter
    def league(self, value):
        self._league = value

    @property
    def sport(self):
        return self._sport or ""

    @sport.setter
    def sport(self, value):
        self._sport = value

    @staticmethod
    def multijoin(url, *parts, seperator="/"):
        return urljoin(url, seperator.join(parts)) + "/"

    @property
    def prefix(self):
        return self.multijoin(
            # Hardcoded for now
            "https://site.api.espn.com/apis/site/v2/sports/", 
            self.league, 
            self.sport
        )

    def request(self, method, suffix, *args, **kwargs):
        url = urljoin(self.prefix, suffix)
        return super().request(method, url, *args, **kwargs)