from day5.inventory import Inventory


def test_nothing_fresh_in_empty_inventory():
    inventory = Inventory()
    assert inventory.is_fresh(10) is False


def test_adding_one_fresh_id_range():
    inventory = Inventory()
    inventory.add_fresh_id_range(5, 7)

    assert inventory.is_fresh(4) is False
    assert inventory.is_fresh(8) is False

    assert inventory.is_fresh(5) is True
    assert inventory.is_fresh(6) is True
    assert inventory.is_fresh(7) is True
