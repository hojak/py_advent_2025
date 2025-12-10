from adv25Tools.problemSolver import ProblemSolver
from day8.playground import Playground


class Solver(ProblemSolver):

    def solve_part1(self):
        playground = Playground.create_from_string(self.parsed_input)

        for step in range(0, 1000):
            pair = playground.get_closest_pair(step)
            playground.connect_boxes(pair[0], pair[1])

        print("We have {} different circuits".format(
            playground.get_number_of_circuits()))

        print("Check Value is: {}".format(playground.get_check_value()))
