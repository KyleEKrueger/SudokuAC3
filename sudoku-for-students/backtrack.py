
"""
We the undersigned promise that we have in good faith attempted to follow the principles of pair programming.
 Although we were free to discuss ideas with others, the implementation is our own. We have shared a common workspace
 (possibly virtually) and taken turns at the keyboard for the majority of the work that we are submitting.
  Furthermore, any non programming portions of the assignment were done independently.
   We recognize that should this not be the case, we will be subject to penalties as outlined in the course syllabus.
   Kyle Krueger & Brett Gallagher
"""
from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)


def consistent(csp, var, val, assignment):
    #Checks if the neighbor has been assigned, and returns false if the value we are assigning has been taken
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment and assignment[neighbor] is val:
            return False
    return True
def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference,
                        verbose=False):
    #Calls backtrack with an empty assignment set
    return backtrack({},csp,select_unassigned_variable,order_domain_values,inference,verbose)

def backtrack(assignment,csp,select_unassigned_variable,order_domain_values,inference,verbose):
    removals = []
    # if all variables assigned, return assignment
    if len(assignment) == len(csp.variables):
        return assignment
    # var = select-unassigned-variable(CSP, assignment)
    var = select_unassigned_variable(assignment, csp)
    # for each value in order-domain-values(var, assignment, csp):
    for val in order_domain_values(var, assignment, csp):
        # if value consistent with assignment:
        if consistent(csp,var,val,assignment):
            # assignment.add ({var = value})
            assignment[var] = val
            removals = csp.suppose(var, val) #flag
            if verbose: print(removals)
            # inferences = inference(CSP, var, assignment)
            inferences = inference(csp, var, val, assignment, removals)
            # if inferences does not equal failure:
            if inferences:
                # assignment.add(inferences)

                # result = backtrack(assignment, CSP)
                result = backtrack(assignment,csp, select_unassigned_variable, order_domain_values, inference, verbose)
                if result != "Failure": return result
        csp.restore(removals)
    return "Failure"

#  """
#  backtracking_search
#     Given a constraint satisfaction problem (CSP),
#     a function handle for selecting variables,
#     a function handle for selecting elements of a domain,
#     and a function handle for making inferences after assignment,
#     solve the CSP using backtrack search
#
#     If verbose is True, prints number of assignments and inferences
#
#     Returns two outputs:
#        dictionary of assignments or None if there is no solution
#        Number of variable assignments made in backtrack search (not counting
#        assignments made by inference)
#     """
#
#     """
#     Backtracking Search Algorithm
#
#     def backtracking-search(CSP):
#         return backtrack({}, CSP); # call w/ no assignments
#
# def backtrack(assignment, CSP):
#     if all variables assigned, return assignment
#     var = select-unassigned-variable(CSP, assignment)
#     for each value in order-domain-values(var, assignment, csp):
#         if value consistent with assignment:
#             assignment.add({var = value})
#             # propagate new constraints (will work without, but probably slowly)
#             inferences = inference(CSP, var, assignment)
#             if inferences ≠ failure:
#                 assignment.add(inferences)
#                 result = backtrack(assignment, CSP)
#                 if result ≠ failure, return result
#             # either value inconsistent or further exploration failed
#             # restore assignment to its state at top of loop and try next value
#             assignment.remove({var = value}, inferences)
#     # No value was consistent with the constraints
#     return failure
#     """




    # See Figure 6.5 of your book for details

    #raise notImplemented
