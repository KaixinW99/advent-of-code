#!/usr/bin/env python
import sys

def solve_lights_gf2(target, buttons):
    """
    Solve the lights-out puzzle using Gaussian elimination over GF(2).
    Using XOR operations to represent toggling lights.
    a ^ (b ^ c) = (a ^ b) ^ c

    This models the problem as a system of linear equations over the binary field:
    Ax = b (mod 2)
    where:
    - A[i][j] = 1 if button j toggles light i
    - x[j] = number of times to press button j (0 or 1)
    - b[i] = target state of light i (0 or 1)
    
    Returns the minimum number of button presses needed.
    """
    n = len(target)  # number of lights
    m = len(buttons)  # number of buttons
    
    # Build augmented matrix [A|b]
    # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    # The augmented matrix will be 
    # [[0 0 0 1]
    #  [0 1 0 1]
    #  [0 0 1 0]
    #  [0 0 1 1]
    #  [1 0 1 0]
    #  [1 1 0 0]
    #  ---------
    #  [0 1 1 0]].T

    matrix = []
    for i in range(n):
        row = [0] * (m + 1)
        for j, button in enumerate(buttons):
            #print("Button:", button)
            if i in button:
                row[j] = 1
        row[m] = target[i]  # augmented column (target state)
        matrix.append(row)
    #print("Augmented Matrix:", matrix)
    
    # Gaussian elimination to row echelon form
    pivot_cols = []
    current_row = 0
    
    for col in range(m):
        # Find pivot (a row with 1 in this column)
        pivot_found = False
        for row in range(current_row, n):
            if matrix[row][col] == 1:
                # Swap rows to bring pivot to current position
                matrix[current_row], matrix[row] = matrix[row], matrix[current_row]
                pivot_found = True
                break
        
        if not pivot_found:
            continue  # This button is redundant/free variable
        
        pivot_cols.append(col)
        
        # Eliminate all other 1s in this column (both above and below)
        for row in range(n):
            if row != current_row and matrix[row][col] == 1:
                # XOR this row with the pivot row
                for c in range(m + 1):
                    matrix[row][c] ^= matrix[current_row][c]
        
        current_row += 1
    #print("Row Echelon Form:", matrix)
    #print("Pivot Columns:", pivot_cols)
    #print("Current Row:", current_row)
    
    # Check for inconsistency (0 = 1, which means no solution)
    for row in range(current_row, n):
        if matrix[row][m] == 1:
            return None  # No solution exists
    
    # Find all free variables (columns without pivots)
    pivot_set = set(pivot_cols)
    free_vars = [col for col in range(m) if col not in pivot_set]
    #print("Free Variables:", free_vars)
    
    # Try all combinations of free variables to find minimum presses
    min_presses = float('inf')
    
    for mask in range(1 << len(free_vars)):
        solution = [0] * m
        
        # Set free variables according to mask
        for i, var in enumerate(free_vars):
            solution[var] = (mask >> i) & 1
            #print("Free Var:", var, "Value:", solution[var])
        #print("Solution after free vars:", solution)

        # Back-substitute to find pivot variables
        for i in range(len(pivot_cols) - 1, -1, -1):
            col = pivot_cols[i]
            solution[col] = matrix[i][m]
            #print("Back-substituting for pivot col:", col, "Initial value:", solution[col])
            for j in range(col + 1, m):
                solution[col] ^= (matrix[i][j] * solution[j])
            #print("Final value for pivot col:", col, "is:", solution[col])
        
        presses = sum(solution)
        min_presses = min(min_presses, presses)
    
    return min_presses


def main():
    total_fewest_button_presses = 0
    
    for case_num, line in enumerate(sys.stdin, 1):
        line = line.strip()
        if not line:
            continue
        
        # Parse input: [lights] (button1) (button2) ... {joltages}
        parts = line.split()
        
        # Extract indicator lights
        ind_light = [0 if light == '.' else 1 for light in parts[0].strip("[]")]
        
        # Extract buttons (skip the last part which is joltages in {})
        buttons = []
        for part in parts[1:]:
            if part.startswith('('):
                button_indices = list(map(int, part.strip("()").split(",")))
                buttons.append(button_indices)
        
        # Solve using Gaussian elimination
        fewest_presses = solve_lights_gf2(ind_light, buttons)
        
        if fewest_presses is None:
            print(f"Case {case_num}: No solution!")
        else:
            #print(f"Case {case_num}: {fewest_presses}")
            total_fewest_button_presses += fewest_presses
    
    print(total_fewest_button_presses)


if __name__ == "__main__":
    main()
