from day9.position import Position
from day9.tileFloor import TileFloor


def test_add_tile():
    floor = TileFloor()
    floor.add_tile(Position(2, 3))
    assert len(floor.tiles) == 1
