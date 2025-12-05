from day5.inventory import Inventory


def test_nothing_fresh_in_empty_inventory():
    inventory = Inventory()
    assert inventory.is_fresh(10) is False