#
# test the code: python opcode_oprands_1.py < input.txt
# check the time: time python opcode_oprands_1.py < input.txt

#! Dijestra is too slow, but I dont know why

from collections import deque

def parse_input(time=1024):
    byte_pos = [tuple(map(int, line.split(","))) for line in open(0).read().splitlines()][:time]
    return byte_pos

def bfs(rows, cols, byte_pos):
    # byte_pos conatins the byte blocks
    q = deque([(0, 0, 0)])
    seen = {(0,0)}
    while q:
        cost, r, c = q.popleft()
        if r == rows and c == cols:
            return cost
        for new_cost, nr, nc in [(cost + 1, r + 1, c), (cost + 1, r, c + 1), (cost + 1, r - 1, c), (cost + 1, r, c - 1)]:
            if nr < 0 or nr > rows or nc < 0 or nc > cols: continue
            if (nr, nc) in seen: continue
            if (nc, nr) in byte_pos: continue
            seen.add((nr, nc))
            q.append((new_cost, nr, nc))

def display(row, col, byte_pos):
    for r in range(row+1):
        for c in range(col+1):
            if (c, r) in byte_pos:
                print("#", end="")
            else:
                print(".", end="")
        print()

def main():
    byte_pos = parse_input(time=1024)
    display(70, 70, byte_pos)
    print(bfs(70, 70, byte_pos))

if __name__ == "__main__":
    main()