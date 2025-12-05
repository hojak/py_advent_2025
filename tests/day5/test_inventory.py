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


def test_adding_two_fresh_id_ranges():
    inventory = Inventory()
    inventory.add_fresh_id_range(20, 21)
    inventory.add_fresh_id_range(5, 7)
    inventory.add_fresh_id_range(9, 10)

    assert inventory.is_fresh(1) is False
    assert inventory.is_fresh(2) is False
    assert inventory.is_fresh(3) is False
    assert inventory.is_fresh(4) is False
    assert inventory.is_fresh(8) is False
    assert inventory.is_fresh(11) is False
    assert inventory.is_fresh(33) is False

    assert inventory.is_fresh(5) is True
    assert inventory.is_fresh(6) is True
    assert inventory.is_fresh(7) is True
    assert inventory.is_fresh(9) is True
    assert inventory.is_fresh(10) is True

    assert inventory.is_fresh(20) is True


def test_adding_range_overlapping_at_end():
    inventory = Inventory()
    inventory.add_fresh_id_range(5, 10)
    inventory.add_fresh_id_range(8, 15)

    assert inventory.fresh_ranges[0] == (5, 15)

    assert inventory.is_fresh(4) is False
    assert inventory.is_fresh(16) is False

    for id in range(5, 16):
        assert inventory.is_fresh(id) is True


def test_adding_range_overlapping_at_start():
    inventory = Inventory()
    inventory.add_fresh_id_range(8, 15)
    inventory.add_fresh_id_range(5, 10)

    assert inventory.fresh_ranges[0] == (5, 15)


def test_adding_range_within_another():
    inventory = Inventory()
    inventory.add_fresh_id_range(5, 10)
    inventory.add_fresh_id_range(7, 9)

    assert inventory.fresh_ranges[0] == (5, 10)


def test_adding_range_enclosing_one_existing():
    inventory = Inventory()
    inventory.add_fresh_id_range(7, 9)
    inventory.add_fresh_id_range(5, 10)

    assert inventory.fresh_ranges[0] == (5, 10)


def test_adding_directly_neighboring_ranges():
    inventory = Inventory()
    inventory.add_fresh_id_range(4, 5)
    inventory.add_fresh_id_range(6, 7)
    inventory.add_fresh_id_range(2, 3)

    assert inventory.fresh_ranges[0] == (2, 7)


def test_mering_two_existing_ranges():
    inventory = Inventory()
    inventory.add_fresh_id_range(2, 3)
    inventory.add_fresh_id_range(6, 7)
    inventory.add_fresh_id_range(4, 5)

    assert inventory.fresh_ranges == [(2, 7)]


def test_merging():
    inventory = Inventory()
    inventory.add_fresh_id_range(1, 4)
    inventory.add_fresh_id_range(7, 8)
    inventory.add_fresh_id_range(10, 12)
    inventory.add_fresh_id_range(3, 11)

    assert inventory.fresh_ranges == [(1, 12)]


def test_get_numer_of_possible_fresh_ids():
    inventory = Inventory()
    inventory.add_fresh_id_range(5, 10)
    inventory.add_fresh_id_range(15, 20)
    inventory.add_fresh_id_range(14, 16)
    
    assert inventory.get_number_of_possible_fresh_ids() == 13
