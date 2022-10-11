# ______________________________________________________________________________
# CSP Backtracking Search

import random
from .util import (first, count)
from constraint_prop import AC3

identity = lambda x: x

argmin = min
argmax = max

def argmin_random_tie(seq, key=identity):
    """Return a minimum element of seq; break ties at random."""
    return argmin(shuffled(seq), key=key)

def shuffled(iterable):
    """Randomly shuffle a copy of iterable."""
    items = list(iterable)
    random.shuffle(items)
    return items

# Variable ordering

def first_unassigned_variable(assignment, csp):
    """The default variable order."""
    return first([var for var in csp.variables if var not in assignment])


def mrv(assignment, csp):
    """Minimum-remaining-values heuristic."""
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))


def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0
                     for val in csp.domains[var])

# Value ordering


def unordered_domain_values(var, assignment, csp):
    """The default value order."""
    return csp.choices(var)


def lcv(var, assignment, csp):
    """Least-constraining-values heuristic."""
    return sorted(csp.choices(var),
                  key=lambda val: csp.nconflicts(var, val, assignment))

# Inference


def no_inference(csp, var, value, assignment, removals):
    return True


def forward_checking(csp, var, value, assignment, removals):
    """Prune neighbor values inconsistent with var=value."""
    
    # Examine neighbors of variable var to be checked
    for B in csp.neighbors[var]:
        # Only worry about neighbor B if it is unassigned
        if B not in assignment:
            # Check each remaining value available to B
            for b in csp.curr_domains[B][:]:
                # Check if current variable var's value is consistent with B=b
                if not csp.constraints(var, value, B, b):
                    # Value is inconsistent, prune from B's domain
                    csp.prune(B, b, removals)
            
            if not csp.curr_domains[B]:
                return False    # Could not be satisfied
    return True


def mac(csp, var, value, assignment, removals):
    """Maintain arc consistency."""
    
    # Uses AC3 algorithm with a list of each neighbor of var    
    return AC3(csp, [(X, var) for X in csp.neighbors[var]], removals)

