from day6.cephalopods_math import CephalopodsMath


def test_simple_sum():
    testee = CephalopodsMath("12\n12\n+ ")

    assert testee.get_result() == 33
