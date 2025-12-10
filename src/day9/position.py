class Position:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def size_of_rectangle_with(self, other: 'Position') -> int:
        width = abs(self.x - other.x)
        height = abs(self.y - other.y)
        return width * height
