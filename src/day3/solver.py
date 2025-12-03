from adv25Tools.problemSolver import ProblemSolver
from day3.highest_joltage import sum_of_joltages


class Solver(ProblemSolver):

    def solve_part1(self):
        print("Result: ", sum_of_joltages(self.parsed_input))
