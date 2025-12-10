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
