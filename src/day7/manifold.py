class Manifold:

    def __init__(self, layout: str):
        self.initial_layout = layout.splitlines()

    def fire_beam(self):
        self.beam_layout = [self.initial_layout[0]]

        for line_index in range(1, len(self.initial_layout)):
            initial_line = self.initial_layout[line_index]
            previous_line = self.beam_layout[line_index - 1]
            beamed_line = self.continue_beams(previous_line, initial_line)
            beamed_line = self.split_beams(previous_line, beamed_line)

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
    
    def split_beams(self, previous_line: str, beamed_line: str) -> str:
        result = beamed_line

        for index in range(0, len(beamed_line)):
            if beamed_line[index] == "^" and previous_line[index] == "|":
                result = Manifold.replace_char_at(result, index, "v")

                if index > 0 and result[index-1] == ".":
                    result = Manifold.replace_char_at(result, index-1, "|")
                
                if index < len(beamed_line) - 1 and result[index+1] == ".":
                    result = Manifold.replace_char_at(result, index+1, "|")

        return result

    def get_beam_layout(self) -> str:
        return "\n".join(self.beam_layout)

    def get_number_of_splitted_beams(self) -> int:
        return "".join(self.beam_layout).count("v")

    def replace_char_at(string: str, index: int, new_char: str) -> str:
        return string[:index] + new_char + string[index + 1:]
