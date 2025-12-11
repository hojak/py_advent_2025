from day9.position import Position


def test_rectangle():
    position_1 = Position(1, 1)
    position_2 = Position(3, 4)

    assert position_1.size_of_rectangle_with(position_2) == 12


def test_positions_are_sortable():
    position_1 = Position(x=1, y=4)
    position_2 = Position(1, 1)
    position_3 = Position(2, 4)
    position_4 = Position(2, 1)

    list = [position_1, position_2, position_3, position_4]

    list.sort()

    assert list == [position_2, position_4, position_1, position_3]


def test_greater_than():
    position_1 = Position(1, 4)
    position_2 = Position(1, 1)
    position_3 = Position(2, 4)
    position_4 = Position(2, 1)

    assert position_1 > position_2
    assert position_3 > position_1
    assert position_3 > position_2
    assert position_4 > position_2
