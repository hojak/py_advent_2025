from day9.position import Position


class TileFloor:
    def __init__(self):
        self.tiles = []
        self.all_rectangl_edges_sorted = []

    def add_tile(self, position: 'Position'):
        self.tiles.append(position)

    def get_size_of_bissgest_rectangle(self) -> int:
        if len(self.all_rectangl_edges_sorted) == 0:
            self.prepare_all_rectangles_sorted()

        if (len(self.all_rectangl_edges_sorted) == 0):
            return 0

        largest_rectangle = self.all_rectangl_edges_sorted[0]
        point1 = self.tiles[largest_rectangle[0]]
        point2 = self.tiles[largest_rectangle[1]]

        return point1.size_of_rectangle_with(point2)

    def prepare_all_rectangles_sorted(self):
        self.all_rectangl_edges_sorted = []
        for first_index in range(len(self.tiles)-1):
            for second_index in range(first_index + 1, len(self.tiles)):
                self.all_rectangl_edges_sorted.append((
                    first_index, second_index
                ))

        self.all_rectangl_edges_sorted.sort(
            key=lambda pair: self.tiles[pair[0]].size_of_rectangle_with(
                self.tiles[pair[1]]
            ),
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
    def is_right_oriented(self) -> bool:
        turns = 0

        work_tiles = self.tiles.copy()
        work_tiles.append(self.tiles[0])
        work_tiles.append(self.tiles[1])

        current_route = work_tiles[1] - work_tiles[0]

        for index in range(2, len(work_tiles)):
            last_route = current_route
            current_route = work_tiles[index] - work_tiles[index - 1]

            if last_route.y == 0:
                if last_route.x > 0:
                    turns += 1 if current_route.y > 0 else -1
                else:
                    turns += -1 if current_route.y > 0 else 1
            else:
                if last_route.y > 0:
                    turns += -1 if current_route.x > 0 else 1
                else:
                    turns += 1 if current_route.x > 0 else -1

        return turns > 0
