from json import dumps

from espyn.client import ESPYN
from espyn.sports import Football
from espyn.sports.leagues import CFB


def test_espyn_client_basic():
    espyn = ESPYN(sport=Football())
    fb = Football()
    assert(fb.league.name in espyn.prefix)
    assert(fb.name in espyn.prefix)

    espyn.sport.league = CFB()
    fb.league = CFB()

    assert(fb.league.name in espyn.prefix)
    assert(fb.name in espyn.prefix)

def test_client_get():
    espyn = ESPYN(sport=Football())
    res = espyn.get("scoreboard")
    assert(res is not None)


def test_client_get_scoreboard():
    espyn = ESPYN(sport=Football())
    res = espyn.get_scoreboard()
    with open("scoreboard.json", "w") as f:
        f.write(dumps(res))
