from day9.position import Position
from day9.tileFloor import TileFloor


def test_add_tile():
    floor = TileFloor()
    floor.add_tile(Position(2, 3))
    assert len(floor.tiles) == 1


def test_get_size_of_biggest_rectangle_of_one():
    floor = TileFloor()
    floor.add_tile(Position(1, 1))
    floor.add_tile(Position(3, 4))

    assert floor.get_size_of_bissgest_rectangle() == 6


def test_get_size_of_biggest_rectangle_of_one():
    floor = TileFloor()
    floor.add_tile(Position(2, 2))
    floor.add_tile(Position(1, 1))
    floor.add_tile(Position(3, 4))

    assert floor.get_size_of_bissgest_rectangle() == 6
