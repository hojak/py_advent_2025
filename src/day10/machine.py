from day10.button import Button
from day10.indicatorLights import IndicatorLights
from day10.joltageStatus import JoltageStatus


class Machine:

    def __init__(self, init_str: str):
        parts = init_str.split(" ")
        self.target_light_configuration = parts[0][1:-1]

        self.indicator_lights = IndicatorLights(
            self.target_light_configuration
        )

        self.init_buttons(parts[1:-1])

        self.target_joltage = [
            int(number) for number in parts[-1][1:-1].split(",")
        ]

    def init_buttons(self, button_definitions: list[str]):
        self.buttons = []
        for definition in button_definitions:
            self.buttons.append(Button(definition[1:-1]))

    def get_indicator_lights(self) -> 'IndicatorLights':
        return self.indicator_lights

    def get_buttons(self) -> list['Button']:
        return self.buttons

    def get_minimal_buttons_for_start(self) -> list[int]:
        sequence = self.shortest_button_sequence_to_light_config(
            '.' * len(self.target_light_configuration),
            self.target_light_configuration
        )

        return sequence

    def shortest_button_sequence_to_light_config(self, start: str, goal: str) \
            -> list[int]:

        found_paths = {start: []}
        queue = [(start, [])]

        while queue:
            (current_lights, path_so_far) = queue.pop(0)

            if current_lights == goal:
                return path_so_far

            lights = IndicatorLights(current_lights)
            for button_index, button in enumerate(self.buttons):
                possible_next_state = lights.push_button(button).status

                if possible_next_state not in found_paths:
                    new_path = path_so_far + [button_index]
                    found_paths[possible_next_state] = new_path
                    queue.append((possible_next_state, new_path))

        return None

    def get_minimal_buttons_for_joltage(self) -> list[int]:
        target_joltage = JoltageStatus(self.target_joltage)
        queue = [(
            JoltageStatus([0] * self.indicator_lights.number_of_lights()),
            []
        )]
        visited = set([queue[0][0]])

        while queue:
            (current_joltage, path_so_far) = queue.pop(0)
            if (current_joltage == target_joltage):
                return path_so_far

            for button_index, button in enumerate(self.buttons):
                possible_next_joltage = current_joltage.push_button(button)
                
                if (possible_next_joltage not in visited
                        and not possible_next_joltage.joltage_to_high_for(target_joltage)):
                    visited.add(possible_next_joltage)
                    new_path = path_so_far + [button_index]
                    queue.append((possible_next_joltage, new_path))
                        
        return None
