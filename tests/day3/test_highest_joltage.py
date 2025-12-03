import pytest
from day3.highest_joltage import highest_joltage, sum_of_joltages


@pytest.mark.parametrize("bank, expected_result", [
    ("987654321", 98),
    ("917654328", 98),
    ("917654320", 97),
    ("117654389", 89),
    ("234234234234278", 78),
    ("818181911112111", 92)
])
def test_highest_joltage(bank, expected_result):
    assert highest_joltage(bank) == expected_result


def test_get_sum_of_joltages():
    assert sum_of_joltages("12\n912\n001215") == 12+92+25
    
