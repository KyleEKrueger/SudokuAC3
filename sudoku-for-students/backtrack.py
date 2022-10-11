

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference,
                        verbose=False):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a function handle for making inferences after assignment,
    solve the CSP using backtrack search

    If verbose is True, prints number of assignments and inferences

    Returns two outputs:
       dictionary of assignments or None if there is no solution
       Number of variable assignments made in backtrack search (not counting
       assignments made by inference)
    """
    
    # See Figure 6.5 of your book for details

    #raise notImplemented
