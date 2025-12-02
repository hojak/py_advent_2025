from day2.idValidator import IdValidator


def test_is_valid_is_true():
    assert IdValidator.is_valid("111000")


def test_is_valid_is_false():
    assert not IdValidator.is_valid("11")
