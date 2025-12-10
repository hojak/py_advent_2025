from day9.position import Position

class TileFloor:
    def __init__(self):
        self.tiles = []

    def add_tile(self, position: 'Position'):
        self.tiles.append(position)