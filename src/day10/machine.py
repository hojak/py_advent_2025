from day10.indicatorLights import IndicatorLights


class Machine:

    def __init__(self, init_str: str):
        self.indicator_lights = IndicatorLights("")
        self.buttons = []

    def get_indicator_lights(self) -> 'IndicatorLights':
        return self.indicator_lights
    
    def get_buttons(self) -> list('Button') :
        return self.buttons
