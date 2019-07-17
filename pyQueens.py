"""N Queens Puzzle Solver"""
import sys


class Nqueens:
    """Solve for all valid solutions of NxN board"""

    def __init__(self, N):
        """Constructor function for Nqueens class"""
        print("Board is %d x %d" % (N, N))
        self.size = N
        self.solutions = 0
        self.solve()

    def solve(self):
        """Function that will call helper functions"""
        board = [[0] * self.size for i in range(self.size)]
        print(board)

    def place_queen(self, board, current_row):
        """Driver function will place a new queen on each row"""
        pass

    def is_valid(self, board, row, column):
        """Helper function to validate position for new queen"""
        pass


def main():
    """Call the solver"""
    n = int(sys.argv[1])
    Nqueens(n)


if __name__ == "__main__":
        # execute only if run as a script
    main()
