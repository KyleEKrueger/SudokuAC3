
from csp_lib.sudoku import (Sudoku, easy1, harder1)
from constraint_prop import AC3
from csp_lib.backtrack_util import mrv, mac, unordered_domain_values
from backtrack import backtracking_search


#s = Sudoku(easy1)
#     s = Sudoku(puzzle)  # construct a Sudoku problem
#     AC3(s);
#for puzzle in [easy1,harder1]:
if True:
    completed = False
    s = Sudoku(harder1)  # construct a Sudoku problem
    completed = AC3(s)
    completed = False
    if completed: print("AC3 used: Puzzle Solved")
    elif not completed:
        completed = backtracking_search(s,mrv,inference = mac, verbose = False)


        # if completed:
        #     print("Backtracking used: Puzzle Solved")

        # else:
        #     print("Unable to solve puzzle")
    s.display(s.infer_assignment())

# solve as much as possible by AC3 then backtrack search if needed
    # using MRV and MAC.
    
    #raise NotImplemented