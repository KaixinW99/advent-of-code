#!/usr/bin/env python
import sys
from scipy.optimize import linprog
import numpy as np

def solve_joltage_linprog(target, buttons):
    """
    Solve using linear programming: minimize sum(x) subject to Ax = b, x >= 0.
    """
    n = len(target)  # number of counters
    m = len(buttons)  # number of buttons
    
    # Build coefficient matrix A
    A = []
    for i in range(n):
        row = [0] * m
        for j, button in enumerate(buttons):
            if i in button:
                row[j] = 1
        A.append(row)
    
    A = np.array(A, dtype=float)
    b = np.array(target, dtype=float)
    
    # Objective: minimize sum of x_j (all coefficients are 1)
    c = np.ones(m)
    
    # Solve: minimize c^T * x subject to A*x = b, x >= 0
    try:
        result = linprog(c, A_eq=A, b_eq=b, bounds=(0, None), method='highs')
        
        if result.success:
            # Round to nearest integer (might have floating point errors)
            solution = np.round(result.x).astype(int)
            # Verify the solution
            if np.allclose(A @ solution, b):
                return int(np.sum(solution))
    except Exception:
        pass
    
    return None


def solve_joltage_gaussian(target, buttons):
    """
    Solve using Gaussian elimination with proper RREF and search over free variables.
    """
    n = len(target)  # number of counters
    m = len(buttons)  # number of buttons
    
    # Build augmented matrix [A|b]
    matrix = []
    for i in range(n):
        row = [0.0] * (m + 1)
        for j, button in enumerate(buttons):
            if i in button:
                row[j] = 1.0
        row[m] = float(target[i])  # augmented column
        matrix.append(row)
    
    # Gaussian elimination to reduced row echelon form (RREF)
    pivot_cols = []
    current_row = 0
    
    for col in range(m):
        # Find pivot (a row with non-zero in this column, starting from current_row)
        pivot_found = False
        best_row = -1
        best_val = 0
        
        for row in range(current_row, n):
            if abs(matrix[row][col]) > 1e-10:  # not zero
                if abs(matrix[row][col]) > best_val:
                    best_val = abs(matrix[row][col])
                    best_row = row
        
        if best_row == -1:
            continue  # This column is free
        
        # Swap rows to bring pivot to current position
        matrix[current_row], matrix[best_row] = matrix[best_row], matrix[current_row]
        pivot_cols.append(col)
        
        # Normalize the pivot row so the pivot is 1
        pivot_val = matrix[current_row][col]
        for c in range(m + 1):
            matrix[current_row][c] /= pivot_val
        
        # Eliminate all other non-zeros in this column (both above and below)
        for row in range(n):
            if row != current_row and abs(matrix[row][col]) > 1e-10:
                factor = matrix[row][col]
                for c in range(m + 1):
                    matrix[row][c] -= factor * matrix[current_row][c]
        
        current_row += 1
    
    # Check for inconsistency (all-zero row with non-zero RHS)
    for row in range(current_row, n):
        if all(abs(matrix[row][c]) < 1e-10 for c in range(m)):
            if abs(matrix[row][m]) > 1e-10:
                return None  # No solution exists
    
    # Find all free variables (columns without pivots)
    pivot_set = set(pivot_cols)
    free_vars = [col for col in range(m) if col not in pivot_set]
    
    # Set all free variables to 0 (minimize total presses)
    solution = [0.0] * m
    
    # Back-substitute to find pivot variables
    for i in range(len(pivot_cols) - 1, -1, -1):
        col = pivot_cols[i]
        solution[col] = matrix[i][m]
        for j in range(col + 1, m):
            if abs(matrix[i][j]) > 1e-10:
                solution[col] -= matrix[i][j] * solution[j]
    
    # Check if solution is valid (all non-negative)
    if any(x < -1e-10 for x in solution):
        return None
    
    # Round to nearest integer and verify
    int_solution = [max(0, int(round(x))) for x in solution]
    
    # Verify the solution
    for i in range(n):
        total = sum(int_solution[j] for j in range(m) if i in buttons[j])
        if total != target[i]:
            return None
    
    return sum(int_solution)


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
        fewest_presses = solve_joltage_gaussian(joltages, buttons)
        
        if fewest_presses is None:
            # Fallback to linear programming
            fewest_presses = solve_joltage_linprog(joltages, buttons)
        
        if fewest_presses is None:
            print(f"Case {case_num}: No solution!")
        else:
            total_fewest_button_presses += fewest_presses
    
    print(total_fewest_button_presses)


if __name__ == "__main__":
    main()
