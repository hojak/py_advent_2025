from adv25Tools.problemSolver import ProblemSolver
from day6.cephalopods_math import CephalopodsMath
from day6.worksheet import Worksheet


class Solver(ProblemSolver):
    def solve_part1(self):
        worksheet = Worksheet()

        for line in self.parsed_input.splitlines():
            if line.count('+') + line.count('*') == 0:
                worksheet.add_line(line)
            else:
                worksheet.set_operants(line)

        print("summing up: ", worksheet.get_grand_total())

    def solve_part2(self):
        math = CephalopodsMath(self.parsed_input)

        print("Result: ", math.get_result())
