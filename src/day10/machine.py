from day10.button import Button
from day10.indicatorLights import IndicatorLights


class Machine:

    def __init__(self, init_str: str):
        parts = init_str.split(" ")
        self.target_light_configuration = parts[0][1:-1]

        self.indicator_lights = IndicatorLights(
            self.target_light_configuration
        )

        self.init_buttons(parts[1:-1])

    def init_buttons(self, button_definitions: list[str]):
        self.buttons = []
        for definition in button_definitions:
            self.buttons.append(Button(definition[1:-1]))

    def get_indicator_lights(self) -> 'IndicatorLights':
        return self.indicator_lights

    def get_buttons(self) -> list['Button']:
        return self.buttons

    def get_minimal_buttons_to_press(self) -> list[int]:
        self.set_up_lightning_graph()

        return []

    def set_up_lightning_graph(self):
        self.graph = {}

        for possible_light_configuration \
                in Machine.create_all_light_configurations(
                    self.indicator_lights.number_of_lights()
                ):
            self.graph[possible_light_configuration] = {}
            
        # todo

    def create_all_light_configurations(length: int) -> list[str]:
        result = ['.', '#']

        for length in range(1, length):
            new_result = []
            for temp in result:
                new_result.append(temp + '.')
                new_result.append(temp + '#')
            result = new_result

        return result
