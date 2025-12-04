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

