import pytest
from day2.idValidator import IdValidator


@pytest.mark.parametrize("id", [
    "111000",
    "101",
    "1",
    "1221",
    "111"
])
def test_is_valid_is_true(id):
    validator = IdValidator()
    assert validator.is_valid(id)


@pytest.mark.parametrize("id", [
    11,
    "1010",
    "10101010",
    "123123"
])
def test_is_valid_is_false(id):
    validator = IdValidator()
    assert not validator.is_valid(id)


@pytest.mark.parametrize("id, number_of_parts", [
    ("1212", 2),
    ("111", 3),
    ("121212", 3),
    ("11111", 5),
    ("123123123123123", 5),
])
def test_is_repeated_pattern_is_true(id, number_of_parts):
    validator = IdValidator()
    assert validator.is_repeated_pattern(id, number_of_parts)


@pytest.mark.parametrize("id, number_of_parts", [
    ("12121", 2),
    ("111", 2),
    ("121212", 2),
])
def test_is_repeated_pattern_is_false(id, number_of_parts):
    validator = IdValidator()
    assert not validator.is_repeated_pattern(id, number_of_parts)


@pytest.mark.parametrize("start, end, expected_result", [
    (11, 22, [11, 22]),
    (95, 115, [99]),
    (998, 1012, [1010]),
    (1188511880, 1188511890, [1188511885]),
    (12, 21, [])
])
def test_get_invalid_ids_from_range(start, end, expected_result):
    validator = IdValidator()
    result = validator.get_invalid_ids(start, end)
    assert expected_result == result


@pytest.mark.parametrize("start, end, number_of_parts, expected_result", [
    (11, 22, 2, [11, 22]),
    (95, 115, 3, [111]),
    (95, 115, 2, [99]),
])
def test_get_invalid_ids_from_range_for_different_part_size(
    start, end, number_of_parts, expected_result
):
    validator = IdValidator([number_of_parts])
    result = validator.get_invalid_ids(start, end)
    assert expected_result == result


def test_get_final_checksum_result():
    validator = IdValidator()
    result = validator.get_checksum("11-22,95-115,12-21")
    assert result == 33 + 99


def test_get_final_checksum_result_with_more_possible_parts():
    validator = IdValidator([2, 3])

    result = validator.get_checksum("11-22,95-115")
    assert result == 11 + 22 + 99 + 111
