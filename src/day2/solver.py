from adv25Tools.problemSolver import ProblemSolver
from day2.idValidator import IdValidator


class Solver(ProblemSolver):

    def solve_part1(self):
        validator = IdValidator()
        result = validator.get_checksum(self.parsed_input)
        print("result: ", result)
