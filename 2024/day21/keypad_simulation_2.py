#
# test the code: python keypad_simulation_1.py < input.txt
# check the time: time python keypad_simulation_1.py < input.txt
from collections import defaultdict, deque
from itertools import product
from functools import cache

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
    dir_lengths = {key: len(value[0]) for key, value in dir_seqs.items()}

    @cache
    def compute_length(seq, depth=2):
        # from button x to y with depth
        # use the recursive function and DFS check with the cache
        if depth == 1: return sum(dir_lengths[(x, y)] for x, y in zip("A"+seq, seq))
        length = 0
        for x, y in zip("A"+seq, seq):
            length += min(compute_length(subseq, depth-1) for subseq in dir_seqs[(x, y)])
        return length
    
    total = 0
    for target, num in parse_input().items():
        inputs = move(target, num_seqs)
        length = min(map(compute_length, inputs))
        total += length * num
    
    print(total)

if __name__ == "__main__":
    main()