"""N Queens Puzzle Solver"""
import sys
import time
from database import Database


class Nqueens:
    """Solve for all valid solutions of NxN board"""

    def __init__(self, N):
        """Constructor function for Nqueens class"""
        self.size = N
        self.solutions = 0
        self.all_boards = []
        self.solve()

    def solve(self):
        """Function that will call helper functions"""
        board = [[0] * self.size for i in range(self.size)]
        t0 = time.time()
        self.place_queens(board, 0)
        t1 = time.time()
        tT = t1 - t0
        print("Found %d solutions in %.3f secs" % (self.solutions, tT))
        self.save_solutions(self.size, self.solutions, self.all_boards)

    def place_queens(self, board, current_row):
        """Recursive driver function will place a new queen on each row"""

        # Base case - when we reach the end of the board
        if current_row == self.size:
            self.print_full_board(board)
            small_board = self.compress_board(board)
            self.all_boards.append(small_board)
            self.solutions += 1
        else:
            """
            This is where the magic happens. We go column by column for each
            row and discard INVALID positions, only moving on when a position
            is valid.
            """
            for column in range(self.size):
                if self.is_valid(board, current_row, column):
                    board[current_row][column] = 1
                    self.place_queens(board, current_row + 1)
                board[current_row][column] = 0

    def is_valid(self, board, row, column):
        """Helper function to validate position for new queen"""
        # Check for column conflicts first. No row conflicts because
        # we go row by row
        for i in range(self.size):
            if board[i][column] == 1 or board[row][i] == 1:
                return False
        """
        Check for diagonal conflicts. Because we go row by row, we only have
        to consider previously placed queens. For each potential new queen,
        we compare its potential position to positions of previous queens.
        """
        for k in range(row):
            for j in range(self.size):
                if board[k][j] == 1 and abs(row - k) == abs(column - j):
                    return False
        return True

    def print_full_board(self, board):
        """Print out the board row by row"""
        for row in range(len(board)):
            print("%s\n" % board[row])
        print("------------------\n")

    def compress_board(self, board):
        compact_board = []
        for row in range(len(board)):
            for position in range(len(board[row])):
                if board[row][position] == 1:
                    compact_board.append(position)
        return compact_board

    def save_solutions(self, n, solutions, boards):
        Database().insertSolutions(n, solutions, boards)


def main():
    """Call the solver"""
    n = int(input("How many queens to solve for? "))
    Nqueens(n)


if __name__ == "__main__":
    # execute only if run as a script
    main()

"""
Citations:
https://www.freecodecamp.org/news/lets-backtrack-and-save-some-queens-1f9ef6af5415/
https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/
https://www.geeksforgeeks.org/n-queen-problem-using-branch-and-bound/
https://www.geeksforgeeks.org/n-queen-in-on-space/
"""
