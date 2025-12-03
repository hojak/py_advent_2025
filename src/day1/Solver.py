from day1.safeDial import SafeDial
from adv25Tools.problemSolver import ProblemSolver


class Solver(ProblemSolver):

    def solve_part1(self):
        sequence = SafeDial.instructions_to_number_sequence(self.parsed_input)
        code = SafeDial.get_code_from_sequence(sequence)

        print("The code for part 1 is:", code)

    def solve_part2(self):
        safe_dial = SafeDial()
        for line in self.parsed_input.splitlines():
            rotation = SafeDial.instruction_to_rotation(line)
            safe_dial.rotate(rotation)

        print("The code for part 2 is: ", safe_dial.get_rotations_over_zero())

