import pytest
from day3.highest_joltage import highest_joltage


@pytest.mark.parametrize("bank, expected_result", [
    ("987654321", 98),
    ("917654328", 98),
    ("917654320", 97),
    ("117654389", 89),
])
def test_highest_joltage(bank, expected_result):
    assert highest_joltage(bank) == expected_result
