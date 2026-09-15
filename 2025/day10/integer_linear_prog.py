#!/usr/bin/env python
import sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csc_matrix

def solve_joltage_milp(target, buttons):
    """
    Solve: minimize sum(x) s.t. A x = b, x integer >= 0
    using scipy.optimize.milp (HiGHS).
    Returns minimal total presses (int), or None if infeasible.
    """
    b = np.asarray(target, dtype=float)
    n = b.size
    m = len(buttons)

    # Build sparse A (n x m) with 0/1 entries
    rows = []
    cols = []
    data = []
    for j, btn in enumerate(buttons):
        for i in btn:
            rows.append(i)
            cols.append(j)
            data.append(1.0)
    A = csc_matrix((data, (rows, cols)), shape=(n, m))

    # Objective: minimize sum x_j
    c = np.ones(m, dtype=float)

    # Tight per-variable upper bounds:
    # x_j <= min(b_i for i in button j)
    ub = np.empty(m, dtype=float)
    for j, btn in enumerate(buttons):
        ub[j] = min(b[i] for i in btn) if btn else 0.0

    bounds = Bounds(lb=np.zeros(m), ub=ub)

    # Equality constraints: A x == b
    constraints = LinearConstraint(A, lb=b, ub=b)

    # All variables integer
    integrality = np.ones(m, dtype=int)

    res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    if not res.success:
        return None

    x = np.rint(res.x).astype(int)
    return int(x.sum())


def main():
    total_fewest_button_presses = 0
    
    for case_num, line in enumerate(sys.stdin, 1):
        line = line.strip()
        if not line:
            continue
        
        # Parse input: [lights] (button1) (button2) ... {joltages}
        parts = line.split()
        
        # Extract buttons and joltages
        buttons = []
        joltages = None
        
        for part in parts[1:]:
            if part.startswith('('):
                button_indices = list(map(int, part.strip("()").split(",")))
                buttons.append(button_indices)
            elif part.startswith('{'):
                joltages = list(map(int, part.strip("{}").split(",")))
        
        if joltages is None:
            print(f"Case {case_num}: Error parsing joltages")
            continue
        
        # Try Gaussian elimination first (more reliable for this problem)
        fewest_presses = solve_joltage_milp(joltages, buttons)
        
        if fewest_presses is None:
            # Fallback to linear programming
            fewest_presses = solve_joltage_milp(joltages, buttons)
        
        if fewest_presses is None:
            print(f"Case {case_num}: No solution!")
        else:
            total_fewest_button_presses += fewest_presses
    
    print(total_fewest_button_presses)


if __name__ == "__main__":
    main()
