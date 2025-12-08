class Manifold:

    def __init__(self, layout: str):
        self.initial_layout = layout.splitlines()

    def fire_beam(self):
        self.beam_layout = [self.initial_layout[0]]
        self.timelines_per_row = [self.intial_timeline_row(self.initial_layout[0])]

        for line_index in range(1, len(self.initial_layout)):
            self.timelines_per_row.append(Manifold.prepare_timeline_row(
                len(self.initial_layout[line_index])
            ))

            beamed_line = self.continue_beams(line_index)
            beamed_line = self.split_beams(line_index, beamed_line)

            self.beam_layout.append(beamed_line)

    def intial_timeline_row(self, first_layout_line: str) -> list[int]:
        result = Manifold.prepare_timeline_row(len(first_layout_line))
        result[first_layout_line.index("S")] = 1
        return result

    def prepare_timeline_row(length: int) -> list[int]:
        return [0 for _ in range(length)]

    def continue_beams(self, current_index: int) -> str:
        previous_line = self.beam_layout[current_index - 1]
        layout_of_current_line = self.initial_layout[current_index]
        result = ""
        for position in range(0, len(layout_of_current_line)):
            if layout_of_current_line[position] == "." and (
                    previous_line[position] == "S"
                    or previous_line[position] == "|"
                    ):
                result += "|"

                self.timelines_per_row[current_index][position] = \
                    self.timelines_per_row[current_index - 1][position]
            else:
                result += layout_of_current_line[position]

        return result

    def split_beams(self,  current_index: int, beamed_line: str) -> str:
        previous_line = self.beam_layout[current_index - 1]
        result = beamed_line

        for index in range(0, len(beamed_line)):
            if beamed_line[index] == "^" and previous_line[index] == "|":
                result = Manifold.replace_char_at(result, index, "v")

                if index > 0 and result[index-1] == ".":
                    result = Manifold.replace_char_at(result, index-1, "|")
                    self.timelines_per_row[current_index][index-1] += 1

                if index < len(beamed_line) - 1 and result[index+1] == ".":
                    result = Manifold.replace_char_at(result, index+1, "|")
                    self.timelines_per_row[current_index][index+1] += 1

        return result

    def get_beam_layout(self) -> str:
        return "\n".join(self.beam_layout)

    def get_number_of_splitted_beams(self) -> int:
        return "".join(self.beam_layout).count("v")

    def get_number_of_timelines(self) -> int:
        return sum(self.timelines_per_row[-1])

    def replace_char_at(string: str, index: int, new_char: str) -> str:
        return string[:index] + new_char + string[index + 1:]
