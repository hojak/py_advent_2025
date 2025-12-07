from day6.tools import transpose_text


def test_transpose():
    result = transpose_text("123\nabc")
    assert result == ["1a", "2b", "3c"]
