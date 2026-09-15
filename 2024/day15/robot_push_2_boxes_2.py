#
# test the code: python robot_push_2_boxes_2.py < input.txt
# check the time: time python robot_push_2_boxes_2.py < input.txt
from copy import deepcopy
def parse_input():
    top, bottom = open(0).read().split("\n\n")
    expansion = {'#': "##", "O": "[]", ".": "..", "@": "@."}
    grids = [list("".join(expansion[char] for char in line)) for line in top.splitlines()]
    moves = "".join(bottom.splitlines())
    return grids, moves


def simulate(grids, moves):
    rows = len(grids)
    cols = len(grids[0])

    # find the position of the robot
    for r in range(rows):
        for c in range(cols):
            if grids[r][c] == "@":
                break
        else:
            continue
        break

    for move in moves:
        dr = {"^": -1, "v": 1}.get(move, 0)
        dc = {"<": -1, ">": 1}.get(move, 0)
        targets = [(r, c)]
        go = True
        for cr, cc in targets:
            nr = cr + dr
            nc = cc + dc
            if (nr, nc) in targets: continue
            char = grids[nr][nc]
            if char == "#":
                go = False
                break
            if char == "[":
                targets.append((nr, nc))
                targets.append((nr, nc+1))
            if char == "]":
                targets.append((nr, nc))
                targets.append((nr, nc-1))
        if not go: continue
        grids_copy = [list(row) for row in grids]   
        grids[r][c] = "."
        grids[r + dr][c + dc] = "@"
        for br, bc in targets[1:]:
            grids[br][bc] = "."
        for br, bc in targets[1:]:
            grids[br + dr][bc + dc] = grids_copy[br][bc]
        r += dr
        c += dc
    return grids

def display(grids):
    for row in grids:
        print(*row, sep="")

def main():
    grids, moves = parse_input()
    rows, cols = len(grids), len(grids[0])
    grids = simulate(grids, moves)
    #display(grids)
    print(sum(100*r+c for r in range(rows) for c in range(cols) if grids[r][c] == "["))

if __name__ == "__main__":
    main()