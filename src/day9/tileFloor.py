from day9.position import Position


class TileFloor:
    def __init__(self):
        self.tiles = []

    def add_tile(self, position: 'Position'):
        self.tiles.append(position)

    def get_size_of_bissgest_rectangle(self) -> int:
        if (len(self.tiles) < 2):
            return 0

        pairs = []
        for first_index in range(len(self.tiles)-1):
            for second_index in range(first_index + 1, len(self.tiles)):
                pairs.append((
                    self.tiles[first_index], self.tiles[second_index]
                ))

        pairs.sort(
            key=lambda pair: pair[0].size_of_rectangle_with(pair[1]),
            reverse=True
        )

        return pairs[0][0].size_of_rectangle_with(pairs[0][1])

    def create_from_string(coordinates: str) -> 'TileFloor':
        floor = TileFloor()

        for line in coordinates.splitlines():
            x_str, y_str = line.strip().split(',')
            x = int(x_str)
            y = int(y_str)
            floor.add_tile(Position(x, y))

        return floor
