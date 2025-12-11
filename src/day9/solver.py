from adv25Tools.problemSolver import ProblemSolver
from day9.tileFloor import TileFloor


class Solver(ProblemSolver):
    def solve_part1(self):
        floor = TileFloor.create_from_string(self.parsed_input)

        print("Number of tiles:", len(floor.tiles))

        print("Size of biggest rectangle:",
              floor.get_size_of_bissgest_rectangle())
