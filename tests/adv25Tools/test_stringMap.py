import pytest

from adv25Tools.stringMap import StringMap
from adv25Tools.coordinates import Coordinates


@pytest.mark.parametrize('init, location, expected', [
    ('aaa\nbbb\nccc', Coordinates(1, 1), 'aaa\nbXb\nccc'),
    ('aaa\nbbb\nccc', Coordinates(0, 0), 'Xaa\nbbb\nccc'),
    ('aaa\nbbb\nccc', Coordinates(2, 2), 'aaa\nbbb\nccX'),
])
def test_set_char_at(init, location, expected):
    testee = StringMap(init)
    testee.set_char_at(location, "X")
    assert str(testee) == expected
