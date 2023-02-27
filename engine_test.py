from engine import Engine

def test_engine_is_singleton():
    eng1 = Engine(None)
    eng2 = Engine(None)

    assert eng1 == eng2, "Engine is a singleton"

