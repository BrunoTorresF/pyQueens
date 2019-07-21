from ..pyQueens import Nqueens
import pytest

solutions = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596, 2279184, 14772512, 95815104, 666090624, 4968057848,
             39029188884, 314666222712, 2691008701644, 24233937684440, 227514171973736, 2207893435808352, 22317699616364044, 234907967154122528]


def test_Nqueens():
    test_instance = Nqueens(4)
    assert test_instance.size == 4
    assert test_instance.solutions == 2


@pytest.mark.parametrize("n, solutions", [(0, 1), (1, 1), (2, 0), (3, 0), (4, 2), (5, 10), (6, 4), (7, 40), (8, 92), (9, 352), (10, 724)])
def test_solutions(n, solutions):
    instance = Nqueens(n)
    assert instance.solutions == solutions
