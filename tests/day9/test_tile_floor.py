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

    assert floor.get_size_of_bissgest_rectangle() == 12


def test_get_size_of_biggest_rectangle():
    floor = TileFloor()
    floor.add_tile(Position(2, 2))
    floor.add_tile(Position(1, 1))
    floor.add_tile(Position(3, 4))

    assert floor.get_size_of_bissgest_rectangle() == 12


def test_create_from_string():
    floor = TileFloor.create_from_string("1,1\n2,2")

    for tile in floor.tiles:
        print(f"Tile at ({tile.x}, {tile.y})")

    assert len(floor.tiles) == 2
    assert floor.get_size_of_bissgest_rectangle() == 4
def test_is_right_oriented():
    floor = TileFloor()

    floor.add_tile(Position(1, 1))
    floor.add_tile(Position(5, 1))
    floor.add_tile(Position(5, 5))
    floor.add_tile(Position(1, 5))

    assert floor.is_right_oriented()


def test_is_not_right_oriented():
    floor = TileFloor()

    floor.add_tile(Position(1, 1))
    floor.add_tile(Position(1, 5))
    floor.add_tile(Position(5, 5))
    floor.add_tile(Position(5, 1))

    assert not floor.is_right_oriented()

