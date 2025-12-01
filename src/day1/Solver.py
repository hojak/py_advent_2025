from day1.safeDial import SafeDial
from adv25Tools.problemSolver import problemSolver


class Solver(problemSolver):

    def solve_part1(self):
        sequence = SafeDial.instructions_to_number_sequence(self.parsed_input)
        code = SafeDial.get_code_from_sequence(sequence)

        print("The code for part 1 is:", code)

