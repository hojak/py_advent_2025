from adv25Tools.problemSolver import ProblemSolver
from day11.network import Network


class Solver(ProblemSolver):

    def solve_part1(self):
        network = Network(self.parsed_input)

        print(
            "Number of possible paths from you to out: ",
            network.get_number_of_possible_paths("you", "out")
        )
