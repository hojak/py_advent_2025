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

    def create_from_string(floor_string: str) -> 'TileFloor':
        floor = TileFloor()

        line_number = 0
        for line in floor_string.splitlines():
            for index, char in enumerate(line):
                if char == '#':
                    floor.add_tile(Position(index, line_number))
            line_number += 1

        return floor
