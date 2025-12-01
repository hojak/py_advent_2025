class SafeDial:
    SIZE_OF_WHEEL = 100

    position: int = 50

    def __init__(self):
        pass

    def rotate(self, amount: int):
        self.position = (self.position + amount) % SafeDial.SIZE_OF_WHEEL
