from espyn.client import ESPYN
from espyn.sports import Football


def test_espyn_client_basic():
    espyn = ESPYN(sport=Football())
    fb = Football()
    assert(fb.league in espyn.prefix)
    assert(fb.name in espyn.prefix)
