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


@pytest.mark.parametrize("instruction, expected_rotation", [
    ("R10", 10),
    ("L10", -10),
    ("R5", 5),
    ("L5", -5),
])
def test_translate_instruction_to_rotation(instruction, expected_rotation):
    assert SafeDial.instruction_to_rotation(instruction) == expected_rotation
