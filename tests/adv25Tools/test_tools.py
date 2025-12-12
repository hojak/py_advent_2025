from adv25Tools.tools import replace_char_at


def test_replace_char_at():
    assert replace_char_at("abcde", 2, "X") == "abXde"
    assert replace_char_at("abcde", 0, "X") == "Xbcde"
    assert replace_char_at("abcde", 4, "X") == "abcdX"
