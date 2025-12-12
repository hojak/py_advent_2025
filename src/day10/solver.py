from adv25Tools.problemSolver import ProblemSolver
from day10.machine import Machine


class Solver(ProblemSolver):

    def solve_part1(self):
        result = 0
        for line in self.parsed_input.splitlines():
            print("Processing line:", line)
            machine = Machine(line)
            minimal_sequence = machine.get_minimal_buttons_sequence()
            result += len(minimal_sequence)
            print("  found sequence:", minimal_sequence)
        
        print("Total minimal buttons to press:", result)