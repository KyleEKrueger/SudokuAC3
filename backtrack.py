'''We the undersigned promise that we have in good faith attempted to follow the principles of pair programming. Although we were free to discuss ideas with others,
 the implementation is our own. We have shared a common workspace (possibly virtually) and taken turns at the keyboard for the majority of the work that we are
  submitting. Furthermore, any non programming portions of the assignment were done independently. We recognize that should this not be the case, we will be subject
   to penalties as outlined in the course syllabus. Kyle Krueger and Brett Gallagher'''

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)


def consistent(csp, var, val, assignment):
    #Checks if the neighbor has been assigned, and returns false if the value we are assigning has been taken
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment.keys() and assignment[neighbor] is val:
            return False
    return True
def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference,
                        verbose=False):
    #Calls backtrack with an empty assignment set
    return backtrack(csp,select_unassigned_variable,order_domain_values,inference,verbose)

def backtrack(csp,select_unassigned_variable,order_domain_values,inference,verbose):
    removals = []
    assignment = csp.infer_assignment()
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
            #csp.nassigns = csp.nassigns + 1
            if verbose: print(removals)
            # inferences = inference(CSP, var, assignment)
            inferences = inference(csp, var, val, assignment, removals)
            # if inferences does not equal failure:
            if inferences:
                # result = backtrack(assignment, CSP)
                result = backtrack(csp, select_unassigned_variable, order_domain_values, inference, verbose)
                if result != "Failure": return result
        csp.restore(removals)
    return "Failure"