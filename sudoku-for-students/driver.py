
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac
from backtrack import backtracking_search


for puzzle in [easy1, harder1]:
    s = Sudoku(puzzle)  # construct a Sudoku problem
    AC3(s);

    # solve as much as possible by AC3 then backtrack search if needed
    # using MRV and MAC.
    
    #raise NotImplemented
