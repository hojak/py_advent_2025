from day10.button import Button
from day10.indicatorLights import IndicatorLights


class Machine:

    def __init__(self, init_str: str):
        parts = init_str.split(" ")
        self.indicator_lights = IndicatorLights(parts[0][1:-1])
        self.buttons = []

    def get_indicator_lights(self) -> 'IndicatorLights':
        return self.indicator_lights
    
    def get_buttons(self) -> list['Button']:
        return self.buttons
