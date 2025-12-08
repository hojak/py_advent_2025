from day6.cephalopods_math import CephalopodsMath


def test_simple_sum():
    testee = CephalopodsMath("12\n12\n+ ")

    assert testee.get_result() == 33


def test_sum_and_multiply():
    testee = CephalopodsMath("12 2  \n12  2 \n+  *  ")

    assert testee.get_result() == 37
