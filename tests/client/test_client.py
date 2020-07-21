from espyn.client import ESPYN
from espyn.sports import Football
from json import dumps

def test_espyn_client_basic():
    espyn = ESPYN(sport=Football())
    fb = Football()
    assert(fb.league in espyn.prefix)
    assert(fb.name in espyn.prefix)

    espyn.sport.league = "college-football"
    fb.league = "college-football"

    assert(fb.league in espyn.prefix)
    assert(fb.name in espyn.prefix)

def test_client_get():
    espyn = ESPYN(sport=Football())
    res = espyn.get("scoreboard")
    json = res.json()
    assert(json is not None)


def test_client_get_scoreboard():
    espyn = ESPYN(sport=Football())
    res = espyn.get_scoreboard()
    json = res.json()
    with open("scoreboard.json", "w") as f:
        f.write(dumps(json))
    pass