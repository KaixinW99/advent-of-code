#
# test the code: python keypad_simulation_1.py < input.txt
# check the time: time python keypad_simulation_1.py < input.txt
from collections import defaultdict, deque
from itertools import product

def parse_input():
    return {line.strip():int(line.strip("A ")) for line in open(0).read().splitlines()}

def compute_seqs(keypad):
    # show the position of each key
    pos = defaultdict(tuple)
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None: pos[keypad[r][c]] = (r, c)
    
    # bfs for the shortest paths
    seqs = defaultdict(list)
    for x in pos:
        for y in pos:
            if x == y:
                seqs[(x, y)] = ["A"]
                continue
            tracks = []
            q = deque([(pos[x], "")])
            optimal = float("inf")
            while q:
                (r, c), moves = q.popleft()
                for nr, nc, nm in [(r-1, c, "^"), (r+1, c, "v"), (r, c-1, "<"), (r, c+1, ">")]:
                    if nr < 0 or nr >= len(keypad) or nc < 0 or nc >= len(keypad[nr]): continue
                    if keypad[nr][nc] is None: continue
                    if keypad[nr][nc] == y:
                        if optimal < len(moves) + 1: break
                        optimal = len(moves) + 1
                        tracks.append(moves + nm + "A")
                    else:
                        q.append(((nr, nc), moves + nm))
                else:
                    continue
                break
            seqs[(x, y)] = tracks
    return seqs
          
def move(target, seqs):
    options = [seqs[(x, y)] for x, y in zip("A" + target, target)]
    #! splat operator to split the list of lists into individual lists
    return ["".join(option) for option in product(*options)]


def main():
    num_keypad = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [None,"0", "A"],
    ]

    num_seqs = compute_seqs(num_keypad)

    dir_keypad = [
        [None, "^", "A"],
        ["<",  "v", ">"],
    ]

    dir_seqs = compute_seqs(dir_keypad)

    total_complexities = 0

    for target, num in parse_input().items():
        robot_1 = move(target, num_seqs)
        next_robot = robot_1
        for _ in range(2):
            possible_next = []
            for seq in next_robot:
                possible_next += move(seq, dir_seqs)
            minlen = min(map(len, possible_next))
            next_robot = [seq for seq in possible_next if len(seq) == minlen]
        total_complexities += len(next_robot[0]) * num
    print(total_complexities)

if __name__ == "__main__":
    main()