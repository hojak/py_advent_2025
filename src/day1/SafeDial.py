class SafeDial:
    position: int = 50

    def __init__(self):
        pass

    def rotate(self, amount: int):
        self.position = self.position + amount
