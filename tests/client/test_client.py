from espyn.client import ESPYN

def test_espyn_client_basic():
    espyn = ESPYN()
    espyn.sport = "quidditch"
    espyn.league = "usq"

    assert("quidditch" in espyn.prefix)
    assert("usq" in espyn.prefix)