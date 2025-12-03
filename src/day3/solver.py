from adv25Tools.problemSolver import ProblemSolver
from day3.bank import Bank


class Solver(ProblemSolver):

    def solve_part1(self):
        print("Result: ", Bank.sum_of_joltages(self.parsed_input))

    def solve_part2(self):
        print("Result: ", Bank.sum_of_joltages(self.parsed_input, 12))
