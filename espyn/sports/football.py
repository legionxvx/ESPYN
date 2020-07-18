from espyn.sports.base import Sport


class Football(Sport):

    def __init__(self):
        super().__init__(
            name="football",
            leagues=[
                "nfl",
                "xfl",
                "college-football"
            ]
        )

        self._league = None

        if self.leagues:
            self._league = self.leagues[0]

    @property
    def league(self):
        return self._league

    @league.setter
    def league(self, value):
        if value not in self.leagues:
            self.leagues.append(value)
            self._league = self.leagues[-1]
            return self._league

        try:
            idx = self.leagues.index(value)
            self._league = self.leagues[idx]
        except (ValueError):
            pass

        return self._league
