from adv25Tools.problemSolver import ProblemSolver
from day5.inventory import Inventory


class Solver(ProblemSolver):

    def parse_input(self) -> list[str]:
        return self.input.split("\n\n")
    
    def solve_part1(self):
        inventory = Inventory()

        for line in self.parsed_input[0].splitlines():
            start_id, end_id = map(int, line.split("-"))
            inventory.add_fresh_id_range(start_id, end_id)

        number_of_fresh_items = 0
        for line in self.parsed_input[1].splitlines():
            id = int(line)

            if inventory.is_fresh(id):
                number_of_fresh_items += 1
                print("found fresh item: ", id)

        print("\nTotally found ", number_of_fresh_items, " fresh items.")
