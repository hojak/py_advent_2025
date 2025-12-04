from adv25Tools.coordinates import Coordinates
from adv25Tools.stringMap import StringMap


class PaperWarehouse(StringMap):
    def __init__(self, layout: str):
        super().__init__(layout)

    def is_occupied(self, x: int, y: int) -> bool:
        return self.get_char_at(Coordinates(x, y)) == '@'

    def is_movable(self, x: int, y: int) -> bool:
        if (not self.is_occupied(x, y)):
            return False
     
        occupied_neighbors = 0
        for location in self.get_neighbor_coordinates(x, y):
            if self.is_occupied(location.x, location.y):
                occupied_neighbors += 1

        return occupied_neighbors <= 4
    
    def get_neighbor_coordinates(self, x: int, y: int) -> list[Coordinates]:
        neighbors = []
        directions = [
            Coordinates(-1, -1), Coordinates(0, -1), Coordinates(1, -1),
            Coordinates(-1, 0), Coordinates(1, 0),
            Coordinates(-1, 1), Coordinates(0, 1), Coordinates(1, 1),
        ]

        for direction in directions:
            position = direction.add(Coordinates(x, y))
            if self.is_within_bounds(position):
                neighbors.append(position)

        return neighbors
