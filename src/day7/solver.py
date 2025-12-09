from adv25Tools.problemSolver import ProblemSolver
from day7.manifold import Manifold


class Solver(ProblemSolver):
    def parse_input(self):
        manifold = Manifold(self.input)
        manifold.fire_beam()

        return manifold

    def solve_part1(self):

        print("Resulting Beams")
        print("---------------")
        print(self.parsed_input.get_beam_layout())
        print(
            "\nNumber of SplittedBeams: ",
            self.parsed_input.get_number_of_splitted_beams()
        )

    def solve_part2(self):
        print("Timelines per Row:")
        print("------------------")
        print(
            "Number of Timelines: ",
            self.parsed_input.get_number_of_timelines()
        )
