"""N Queens Puzzle Solver"""
import sys


class Nqueens:
    """Solve for all valid solutions of NxN board"""

    def __init__(self, N):
        print("Board is %d x %d" % (N, N))
        pass

    def solve(self, parameter_list):
        pass

    def place_queen(self, parameter_list):
        pass

    def is_valid(self, parameter_list):
        pass


def main():
    """Call the solver"""
    n = int(sys.argv[1])
    Nqueens(n)


if __name__ == "__main__":
        # execute only if run as a script
    main()
