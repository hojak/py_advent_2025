import pytest
from day1.safeDial import SafeDial


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


def test_instructions_to_number_sequence():
    instructions = '''L68
L30
R48
L5'''
    expected = [50, 82, 52, 0, 95]
    assert SafeDial.instructions_to_number_sequence(instructions) == expected


@pytest.mark.parametrize("sequence, expected_code", [
    ([50, 82, 52, 0, 95], 1),
    ([50, 0, 52, 0, 0], 3),
    ([50, 82, 52, 1, 2, 3, 95], 0)
])
def test_get_code_from_sequence(sequence, expected_code):
    assert SafeDial.get_code_from_sequence(sequence) == expected_code


@pytest.mark.parametrize("rotations, expected_result", [
    ([], 0),
    ([49], 0),
    ([50], 1),
    ([150], 2),
    ([10, 40], 1),
    ([-49], 0),
    ([-50], 1),
    ([-150], 2)
])
def test_count_rotations_over_zero(rotations, expected_result):
    testee = SafeDial()

    for rotation in rotations:
        testee.rotate(rotation)

    assert testee.get_rotations_over_zero() == expected_result

