from day4.paperWarehouse import PaperWarehouse


def test_create_warehouse():
    testee = PaperWarehouse("@..@\n....\n@@@@")
    assert testee.width == 4
    assert testee.height == 3
