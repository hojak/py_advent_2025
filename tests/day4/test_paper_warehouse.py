import pytest
from day4.paperWarehouse import PaperWarehouse


def test_create_warehouse():
    testee = PaperWarehouse("@..@\n....\n@@@@")
    assert testee.width == 4
    assert testee.height == 3


def test_is_occupied():
    testee = PaperWarehouse("@..@\n....\n@@@@")
    assert testee.is_occupied(0, 0) is True
    assert testee.is_occupied(1, 0) is False
    assert testee.is_occupied(2, 0) is False
    assert testee.is_occupied(3, 0) is True

    assert testee.is_occupied(0, 1) is False
    assert testee.is_occupied(1, 1) is False
    assert testee.is_occupied(2, 1) is False
    assert testee.is_occupied(3, 1) is False

    assert testee.is_occupied(0, 2) is True
    assert testee.is_occupied(1, 2) is True
    assert testee.is_occupied(2, 2) is True
    assert testee.is_occupied(3, 2) is True


@pytest.mark.parametrize("layout, x, y, expected", [
    ("@@.\n@.@\n...", 1, 1, False),
    ("@@.\n@@@\n...", 1, 1, True),
    ("@@.\n@@@\n.@.", 1, 1, False),
    ("@@.\n@@@\n.@.", 0, 0, True),
    ("@@@\n@@@\n.@.", 1, 0, False),

])
def test_is_movable(layout, x, y, expected):
    testee = PaperWarehouse(layout)
    assert testee.is_movable(x, y) is expected
