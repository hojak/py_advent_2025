import sys
import importlib


def main(day: str, input_file) -> None:
    module_name = f"day{day}.solver"
    module = importlib.import_module(module_name)
    solver_class = getattr(module, 'Solver')

    solver = solver_class("data/day"+day+"/"+input_file)

    solver.execute()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
