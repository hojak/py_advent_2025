from adv25Tools.problemSolver import ProblemSolver
from day2.idValidator import IdValidator


class Solver(ProblemSolver):

    def solve_part1(self):
        validator = IdValidator()
        result = validator.get_checksum(self.parsed_input)
        print("result: ", result)

    def solve_part2(self):
        validator = IdValidator([2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = validator.get_checksum(self.parsed_input)
        print("result: ", result)
