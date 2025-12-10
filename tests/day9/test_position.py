from day9.position import Position


def test_rectangle():
    position_1 = Position(1, 1)
    position_2 = Position(3, 4)

    assert position_1.size_of_rectangle_with(position_2) == 12
