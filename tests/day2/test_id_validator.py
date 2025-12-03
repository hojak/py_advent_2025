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
    assert IdValidator.is_valid(id)


@pytest.mark.parametrize("id", [
    11,
    "1010",
    "10101010",
    "123123"
])
def test_is_valid_is_false(id):
    assert not IdValidator.is_valid(id)


def test_get_invalid_ids_from_range():
    result = IdValidator.get_invalid_ids(1, 22)
    assert [11, 22] == result
