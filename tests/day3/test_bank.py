import pytest
from day3.bank import Bank


@pytest.mark.parametrize("bankstr, expected_result", [
    ("987654321", 98),
    ("917654328", 98),
    ("917654320", 97),
    ("117654389", 89),
    ("234234234234278", 78),
    ("818181911112111", 92)
])
def test_highest_joltage(bankstr, expected_result):
    bank = Bank(bankstr)
    assert bank.highest_joltage() == expected_result


@pytest.mark.parametrize("bankstr, size, expected_result", [
    ("987654321", 2, 98),
    ("1", 1, 1),
    ("11", 2, 11),
    ("111", 3, 111),
    ("2212", 3, 222),
    ("987654321111111", 12, 987654321111),
    ("234234234234278", 12, 434234234278)
])
def test_highest_joltage_with_size(bankstr, size, expected_result):
    bank = Bank(bankstr)
    assert bank.highest_joltage(size) == expected_result


def test_get_sum_of_joltages():
    assert Bank.sum_of_joltages("12\n912\n001215") == 12+92+25
    
    
def test_get_sum_of_joltages_with_size():
    assert Bank.sum_of_joltages("987654321111111\n234234234234278", 12) == 987654321111 + 434234234278
    
