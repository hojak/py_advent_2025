from adv25Tools.problemSolver import ProblemSolver
from day5.inventory import Inventory


class Solver(ProblemSolver):

    def parse_input(self) -> list[str]:
        result = self.input.split("\n\n")

        self.inventory = Inventory()

        for line in result[0].splitlines():
            start_id, end_id = map(int, line.split("-"))
            self.inventory.add_fresh_id_range(start_id, end_id)

        return result

    def solve_part1(self):
        number_of_fresh_items = 0
        for line in self.parsed_input[1].splitlines():
            id = int(line)

            if self.inventory.is_fresh(id):
                number_of_fresh_items += 1
                print("found fresh item: ", id)

        print("\nTotally found ", number_of_fresh_items, " fresh items.")

    def solve_part2(self):
        result = self.inventory.get_number_of_possible_fresh_ids()
        print("Number of possible ids of fresh items: ", result)
