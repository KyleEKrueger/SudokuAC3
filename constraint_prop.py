'''
Constraint propagation
'''

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation

    csp - constraint satisfaction problem
    queue - list of constraints (might be None in which case they are
        populated from csp's variable list (len m) and neighbors (len k1...km):
        [(v1, n1), (v1, n2), ..., (v1, nk1), (v2, n1), (v2, n3), ... (v2, nk2),
         (vm, n1), (vk, n2), ..., (vk, nkm) ]
    removals - List of variables and values that have been pruned.  This is only
        useful for backtracking search which will enable us to restore things
        to a former point

    returns
        True - All constraints have been propagated and hold
        False - A variables domain has been reduced to the empty set through
            constraint propagation.  The problem cannot be solved from the
            current configuration of the csp.
    """
    #Queue creation
    if queue is None:
        queue = []
        for i in csp.variables:
            neighborsOfI = csp.neighbors[i]
            for j in neighborsOfI:
                newTuple = (i,j)
                queue.append(newTuple)

    # Queue up binary arcs
    #csp.display(csp.infer_assignment())
    #print(csp.constraints)
    
    #While the queue isn't empty
    while not (len(queue) == 0):
            # (Xi,Xj) = queue.dequeue() #get binary constraints
        Xi,Xj = queue.pop()
            #print(Xi,Xj)

        #if revise(CSP, xi,xj):
        if revise(csp,Xi,Xj,removals):
            if len(csp.curr_domains[Xi]) == 0:
                # if domain(xi) is not empty return false
                #csp.display(csp.infer_assignment())
                #print("Returning False!")
                return False
            # else
            #   for each (xk) in {neighbors(xi)-xj}
            #   queue.enqueue(xk,xi)
            else:
                for x in csp.neighbors[Xi]:
                    if x == Xj:
                        continue
                    else:
                        queue.append((x, Xi))
    #csp.display(csp.infer_assignment())
    return True


def revise(csp, Xi, Xj, removals):
    """Return true if we remove a value.
    Given a pair of variables Xi, Xj, check for each value i in Xi's domain
    if there is some value j in Xj's domain that does not violate the
    constraints.

    csp - constraint satisfaction problem
    Xi, Xj - Variable pair to check
    removals - list of removed (variable, value) pairs.  When value i is
        pruned from Xi, the constraint satisfaction problem needs to know
        about it and possibly updated the removed list (if we are maintaining
        one)
    """
    if removals == None:
        removals = []
    #revised = false
    revised = False
    #for each x in domain xi
    for x in csp.curr_domains[Xi]:
        constraintSatisifed = False
        #if there isn't a y that exists such that it is contained in the domain xj such that constraint holds between x and y
        for y in csp.curr_domains[Xj]:
            if csp.constraints(Xi,x,Xj,y):
                constraintSatisifed = True
            #delete x from domain xi
        if not constraintSatisifed:
            csp.prune(Xi,x,removals)
            # revised = true
            revised = True
    #return revised
    return revised