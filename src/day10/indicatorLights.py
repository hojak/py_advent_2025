from day7.manifold import Manifold


class IndicatorLights:

    def __init__(self, init_string: str):
        self.status = init_string

    def number_of_lights(self) -> int:
        return len(self.status)

    def push_button(self, button) -> 'IndicatorLights':
        new_status = self.status
        for switch_light in button.connected_lights:
            new_light_status = '#' if new_status[switch_light] == '.' else '.'
            new_status = Manifold.replace_char_at(
                new_status, switch_light, new_light_status)

        return IndicatorLights(new_status)

    def __str__(self) -> str:
        return self.status
