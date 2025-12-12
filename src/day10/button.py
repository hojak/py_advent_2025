class Button:

    def __init__(self, init_string: str):
        self.connected_lights = [
            int(number) for number in init_string.split(",")
        ]
