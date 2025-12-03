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
    assert validator.is_valid_instance(id)


@pytest.mark.parametrize("id", [
    11,
    "1010",
    "10101010",
    "123123"
])
def test_is_valid_is_false(id):
    validator = IdValidator()
    assert not validator.is_valid_instance(id)


@pytest.mark.parametrize("start, end, expected_result", [
    (11, 22, [11, 22]),
    (95, 115, [99]),
    (998, 1012, [1010]),
    (1188511880, 1188511890, [1188511885]),
    (12, 21, [])
])
def test_get_invalid_ids_from_range(start, end, expected_result):
    result = IdValidator.get_invalid_ids(start, end)
    assert expected_result == result


def test_get_final_checksum_result():
    result = IdValidator.get_checksum("11-22,95-115,12-21")
    assert result == 33 + 99
