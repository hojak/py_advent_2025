class IndicatorLights:

    def __init__(self, init_string: str):
        self.lights_are_on = []

        for index in range(0, len(init_string)):
            self.lights_are_on.append(False)

    def number_of_lights(self) -> int:
        return len(self.lights_are_on)
