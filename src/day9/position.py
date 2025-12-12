class Position:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def size_of_rectangle_with(self, other: 'Position') -> int:
        width = abs(self.x - other.x) + 1
        height = abs(self.y - other.y) + 1
        return width * height

    def __lt__(self, other: 'Position') -> bool:
        if (self.y == other.y):
            return self.x < other.x
        else:
            return self.y < other.y

    def __gt__(self, other: 'Position'):
        if (self.y == other.y):
            return self.x > other.x
        else:
            return self.y > other.y

    def __eq__(self, other: 'Position'):
        return self.x == other.x and self.y == other.y

    def __le__(self, other: 'Position'):
        return not self.__gt__(other)

    def __ge__(self, other: 'Position'):
        return not self.__lt__(other)

    def __ne__(self, other: 'Position'):
        return not self.__eq__(other)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __sub__(self, other: 'Position') -> 'Position':
        return Position(self.x - other.x, self.y - other.y)

