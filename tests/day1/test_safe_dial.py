import pytest
from day1.SafeDial import SafeDial


def test_create_dial():
    testee = SafeDial()
    assert testee is not None
    assert testee.position == 50


@pytest.mark.parametrize("amount, expected_position", [
    (10, 60),
    (-10, 40),
    (50, 0),
    (-50, 0),
    (-51, 99)
])
def test_rotate(amount, expected_position):
    testee = SafeDial()
    testee.rotate(amount)
    assert testee.position == expected_position
