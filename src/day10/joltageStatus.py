class JoltageStatus:

    def __init__(self, status: list[int]):
        self.status = status

    def __str__(self) -> str:
        return "["+','.join(self.status)+"]"

    def push_button(self, button) -> 'JoltageStatus':
        new_status = self.status.copy()
        for switch_index in button.connected_lights:
            new_status[switch_index] += 1

        return JoltageStatus(new_status)

    def joltage_to_high_for(self, target_joltage: list[int]) -> bool:
        for index, joltage in enumerate(target_joltage):
            if self.status[index] > joltage:
                return True
        return False

    def __eq__(self, other: 'JoltageStatus') -> bool:
        return self.status == other.status
