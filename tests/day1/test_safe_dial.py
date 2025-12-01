from day1.SafeDial import SafeDial


def test_create_dial():
    testee = SafeDial()
    assert testee is not None
    assert testee.position == 50
