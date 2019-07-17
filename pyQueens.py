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
        self.place_queen(board, 0)
        print("Found %d solutions" % self.solutions)

    def place_queen(self, board, current_row):
        """Driver function will place a new queen on each row"""
        if current_row == self.size:
            print(board)
            self.solutions += 1
        else:
            for column in range(self.size):
                if self.is_valid(board, current_row, column):
                    board[current_row][column] = 1
                    self.place_queen(board, current_row + 1)

    def is_valid(self, board, row, column):
        """Helper function to validate position for new queen"""
        for i in range(len(board)):
            if board[row][i] == 1 or board[i][column] == 1:
                return False
            # for j in range(len(board)):
            #     if i + j == row + column:
            #         return False
        return True


def main():
    """Call the solver"""
    n = int(sys.argv[1])
    Nqueens(n)


if __name__ == "__main__":
        # execute only if run as a script
    main()
