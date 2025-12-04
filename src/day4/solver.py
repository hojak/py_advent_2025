from adv25Tools.problemSolver import ProblemSolver
from day4.paperWarehouse import PaperWarehouse


class Solver(ProblemSolver):

    def solve_part1(self) -> str:
        warehouse = PaperWarehouse(self.parsed_input)
        print("Result: ", warehouse.number_of_movable_rolls())
