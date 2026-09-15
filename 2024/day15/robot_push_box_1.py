#
# test the code: python robot_push_box_1.py < input.txt
# check the time: time python robot_push_box_1.py < input.txt

def parse_input():
    top, bottom = open(0).read().split("\n\n")
    grids = [list(line) for line in top.splitlines()]
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
        cr, cc = r, c
        go = True
        while True:
            cr += dr
            cc += dc
            char = grids[cr][cc]
            if char == "#":
                go = False
                break
            if char == "O":
                targets.append((cr, cc))
            if char == ".":
                break
        if not go: continue # it involves the situation >: #...@OO#
        grids[r][c] = "."
        grids[r + dr][c + dc] = "@"
        for br, bx in targets[1:]:
            grids[br + dr][bx + dc] = "O"
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
    print(sum(100*r+c for r in range(rows) for c in range(cols) if grids[r][c] == "O"))

if __name__ == "__main__":
    main()