from adv25Tools.coordinates import Coordinates
from adv25Tools.stringMap import StringMap


class PaperWarehouse(StringMap):
    def __init__(self, layout: str):
        super().__init__(layout)

    def is_occupied(self, x: int, y: int) -> bool:
        return self.get_char_at(Coordinates(x, y)) == '@'
