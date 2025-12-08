from day6.tools import transpose_text


def test_transpose():
    result = transpose_text("123\nabc")
    assert result == ["1a", "2b", "3c"]


def test_transpose_complex():
    text = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  '''

    result = transpose_text(text)

    expected = [
        "1  *", "24  ", "356 ", "    ",
        "369+", "248 ", "8   ", "    ",
        " 32*", "581 ", "175 ", "    ",
        "623+", "431 ", "  4 "
    ]

    assert result == expected
