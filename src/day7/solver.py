from adv25Tools.problemSolver import ProblemSolver
from day7.manifold import Manifold


class Solver(ProblemSolver):
    def solve_part1(self):
        manifold = Manifold(self.parsed_input)
        manifold.fire_beam()

        print("Resulting Beams")
        print("---------------")
        print(manifold.get_beam_layout())
        print(
            "\nNumber of SplittedBeams: ",
            manifold.get_number_of_splitted_beams()
        )
