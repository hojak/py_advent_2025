from adv25Tools.problemSolver import ProblemSolver
from day2.idValidator import IdValidator


class Solver(ProblemSolver):

    def solve_part1(self):
        result = IdValidator.get_checksum(self.parsed_input)
        print("result: ", result)
