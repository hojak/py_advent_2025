class Manifold:

    def __init__(self, layout: str):
        self.initial_layout = layout.splitlines()

    def fire_beam(self):
        self.beam_layout = [self.initial_layout[0]]

        for line_index in range(1, len(self.initial_layout)):
            initial_line = self.initial_layout[line_index]
            previous_line = self.beam_layout[line_index - 1]

            beamed_line = self.continue_beams(previous_line, initial_line)

            self.beam_layout.append(beamed_line)

    def continue_beams(self, previous_line: str, layout_of_current_line: str) -> str:
        result = ""
        for position in range(0, len(layout_of_current_line)):
            if layout_of_current_line[position] == "." and (
                    previous_line[position] == "S"
                    or previous_line[position] == "|"
                    ):
                result += "|"
            else:
                result += layout_of_current_line[position]

        return result

    def get_beam_layout(self) -> str:
        return "\n".join(self.beam_layout)

    def get_number_of_splitted_beams(self) -> int:
        return 0
