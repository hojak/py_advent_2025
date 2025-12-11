from day9.position import Position


class TileFloor:
    def __init__(self):
        self.tiles = []
        self.all_rectangles_sorted = []

    def add_tile(self, position: 'Position'):
        self.tiles.append(position)

    def get_size_of_bissgest_rectangle(self) -> int:
        if len(self.all_rectangles_sorted) == 0:
            self.prepare_all_rectangles_sorted()
            
        if (len(self.all_rectangles_sorted) == 0):
            return 0

        largest_rectangle = self.all_rectangles_sorted[0]
        return largest_rectangle[0].size_of_rectangle_with(largest_rectangle[1])
    
    def prepare_all_rectangles_sorted(self):
        self.all_rectangles_sorted = []
        for first_index in range(len(self.tiles)-1):
            for second_index in range(first_index + 1, len(self.tiles)):
                self.all_rectangles_sorted.append((
                    self.tiles[first_index], self.tiles[second_index]
                ))

        self.all_rectangles_sorted.sort(
            key=lambda pair: pair[0].size_of_rectangle_with(pair[1]),
            reverse=True
        )

    def create_from_string(coordinates: str) -> 'TileFloor':
        floor = TileFloor()

        for line in coordinates.splitlines():
            x_str, y_str = line.strip().split(',')
            x = int(x_str)
            y = int(y_str)
            floor.add_tile(Position(x, y))

        return floor
