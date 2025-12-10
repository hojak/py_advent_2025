from math import sqrt


class JunctionBox:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def distance_to(self, other: object) -> float:
        return sqrt(
            (self.x - other.x) ** 2
            + (self.y-other.y) ** 2
            + (self.z - other.z) ** 2
        )

    def __eq__(self, value):
        return type(value) is JunctionBox and \
            self.x == value.x and self.y == value.y and self.z == value.z

    def __str__(self):
        return "JunctionBox({},{},{})".format(self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))
