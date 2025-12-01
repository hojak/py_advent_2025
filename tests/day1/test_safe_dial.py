from day1.SafeDial import SafeDial
import pytest

def test_create_dial():
    testee = SafeDial()
    assert testee != None