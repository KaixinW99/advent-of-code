# Explain the code

# Day 1:
It involves the knowledge of modulo.
For the second part, we need to self define a divmod function.
As the built-in divmod function does not work with negative numbers in the way we want.
L50 from 50, gives 0 and 1 hit to 0. however, divmod(50-50, 100) gives (0, 0).
Thats why we need to switch the 0 to N in case of first being 0.

# Day 2;
It involves the knowledge of string.
For the second part, we need to build is_repeaded_seqeunce().
The algorithm involves the loop from len = 1 to length//2+1
if length is divisible by len, we check if s[0:len] * (length//len) == s.

# Day 3:
It involves the knowledge of max function.
For the second part, we set up a max function ourselves.
We set remaining for the number we can select, 
and we have pos and end idx to search the each largest digit one by one.

# Day 4:
It involves the knowledge of for loop.
For the second part, we set up an outside loop for mulitiple removing process.

# Day 5:
It involves the knowledge of merging ranges.
For the second part, it takes too much time to union all the ranges with set.
Therefore, we use a merging algorithm.
Then, sort the list and it will give the interval list in ascending first character.
First, we save all the intervals into list.
Finally, we can merge the end point one by one and output the merge list.

# Day 6:
It involves the knowledge of eval() and ljust()
The second part of the question needs reading data based on vertial alignment.

# Day 7:
It involves the knowledge of simulation and DFS (dynamic coding skills)
The second part is a very good example of recording or counting all the pathways

# Day 8:
## part 1
- "DSU" stands for Disjoint-Set Union (also called Union-Find). It's a data structure to keep track of a partition of elements into disjoint groups (sets), supporting:
  - find(x): which set (representative/root) x belongs to,
  - union(a,b): merge the sets containing a and b.
- It's used for connectivity problems: quickly answer "are these two items already connected?" and merge groups efficiently.

Now a focused walk-through of your `find` and `union` implementations, with concrete examples and an easy debug helper you can run.

1) Data representation
- self.p: parent pointer array. For each element x, p[x] is its parent; roots satisfy p[root] == root.
- self.sz: size array. For a root r, sz[r] = number of elements in the component whose root is r. Non-root entries of sz may be stale/unused.

2) find(x) — what it does and why
Your code (path-halving variant):

```python
def find(self, x):
    while self.p[x] != x:
        self.p[x] = self.p[self.p[x]]   # point x to its grandparent
        x = self.p[x]                   # move x upward
    return x
```

- Goal: return the root of x's set.
- How it works: while x is not a root, set x's parent to its grandparent (halving the path), then continue from the parent.
- Effect: it shortens the path from x to its root (each visited node moves closer to the root), making future finds faster.
- It's iterative (no recursion) and very efficient in practice.

Example trace (step-by-step)
Start with parent array representing a chain 0 <- 1 <- 2 <- 3:
- p = [0, 0, 1, 2]  (meaning: 1→0, 2→1, 3→2)

Call find(3):
- Iteration 1:
  - x = 3, p[3] = 2 (not root)
  - set p[3] = p[p[3]] = p[2] = 1  → p becomes [0,0,1,1]
  - set x = p[3] = 1
- Iteration 2:
  - x = 1, p[1] = 0 (not root)
  - set p[1] = p[p[1]] = p[0] = 0 → p stays [0,0,1,1] (1 now points to 0)
  - set x = p[1] = 0
- Now p[x] == x so loop ends; find returns 0.

After one find(3) call, p = [0,0,1,1] — node 3 now reaches root in two hops (was 3). Calling find(3) again will make p[3] become 0 directly.

Compare to recursive full compression (optional)
Full compression sets every node on the path directly to the root in one call:

```python
def find(self, x):
    if self.p[x] != x:
        self.p[x] = self.find(self.p[x])
    return self.p[x]
```

- That flattens the entire path in one go (p becomes [0,0,0,0] in the example). Path-halving approximates this iteratively but avoids recursion.

3) union(a, b) — what it does and why
Your code:

```python
ra = self.find(a)
rb = self.find(b)
if ra == rb:
    return False                 # already same component
if self.sz[ra] < self.sz[rb]:
    ra, rb = rb, ra              # ensure ra is the bigger root
self.p[rb] = ra                 # attach smaller under larger
self.sz[ra] += self.sz[rb]      # update size
return True
```

- Steps:
  1. Find roots ra and rb.
  2. If equal, a and b are already connected — nothing to do (returns False).
  3. Otherwise attach the smaller tree under the larger root (union by size). This keeps tree heights small.
  4. Update the root's size and return True (success).

Concrete example: union(1,2) starting from p=[0,0,0,0], sz=[1,1,1,1]
- find(1) -> root 0 (depending on current state) — but imagine separate sets so initial roots are themselves.
- After union, parent pointer and size updated for the root.

4) Why union returns True/False is useful
- True means the union merged two different components (connectivity changed).
- False means the edge is redundant (both endpoints already in same set). Use this to skip counting redundant connections (your earlier question).

5) Small Python debug helper you can paste and run
Add this to your file (or run in REPL) — it shows parent array and returns:

```python
def debug_ops():
    d = DSU(6)
    print("initial p", d.p, "sz", d.sz)
    print("union(0,1):", d.union(0,1), "-> p", d.p, "sz", d.sz)
    print("union(2,3):", d.union(2,3), "-> p", d.p, "sz", d.sz)
    print("union(1,2):", d.union(1,2), "-> p", d.p, "sz", d.sz)
    print("union(3,0):", d.union(3,0), "-> p", d.p, "sz", d.sz)  # should be False
    print("find(5):", d.find(5), "p", d.p)
    print("find(3):", d.find(3), "p", d.p)
```

Run it in a small script to observe how parents/sizes evolve.

6) Visual intuition
- Think of each component as a rooted tree. `p` points toward the root. `find` climbs to the root and compresses paths. `union` attaches one root under another, preferring the larger root as the new parent to keep depths small.

7) Complexity (brief)
- With union by size/rank and path-halving (or full path compression), each operation is nearly O(1) amortized — more precisely O(α(n)) where α is the inverse Ackermann function (very small).

If you'd like, I can:
- Add a debug flag to distance.py to print parent arrays after each union/find so you can watch live,
- Replace path-halving with recursive full path compression for simpler immediate flattening,
- Or add more worked examples (drawn parent arrays) tailored to particular sequences of unions you care about.

# Day 9:
**coordinate-compression + scanline**
1. A short explanation of the idea.
2. A complete Python program that:

   * Uses coordinate compression.
   * Fills an “inside the loop” grid.
   * Uses a 2D prefix sum to check whether a rectangle is fully inside.
   * Tries all pairs of red tiles as opposite corners (like your part 1) but checks the interior efficiently.

---

## Idea in plain terms

We have:

* A list of red tiles `(x, y)` in **path order** that forms a closed orthogonal polygon.
* All tiles on the path + all tiles inside that loop are green.
* For part 2, we want the largest rectangle with opposite corners red and the **entire rectangle** inside the loop.

Brute force per tile is impossible because coordinates are up to ~100k.

### Step 1: Coordinate compression

Let:

```python
xs = sorted(unique x of all red points)
ys = sorted(unique y of all red points)
```

We don’t care about every integer between min and max; the polygon only changes at these coordinates.
Between `xs[i]` and `xs[i+1]` the geometry is uniform; same for `ys`.

This defines a grid of **cells**:

* Column `i` represents the x-interval `[xs[i], xs[i+1]]`
* Row `j` represents the y-interval `[ys[j], ys[j+1]]`

Each cell `(j, i)` is a small axis-aligned rectangle in continuous space.

### Step 2: Mark which cells are inside the polygon

We treat the ordered red tiles as vertices of a polygon (closing the loop from last to first) and extract all **vertical edges** `(x, y1, y2)`.

For each row band `j`:

* Take a horizontal line at `y_mid = (ys[j] + ys[j+1]) / 2`.
* Find all vertical edges that intersect this line (`y1 <= y_mid < y2`).
* Their x-coordinates form a sorted list `inter_x = [x0, x1, x2, x3, ...]`.
* By the even–odd rule, the polygon interior on that scanline lies between pairs:

  * `[x0, x1]`, `[x2, x3]`, …

For each interval `[xL, xR]` we find the compressed column indices:

```python
iL = index_of(xL in xs)
iR = index_of(xR in xs)
```

Then all cells `inside[j][i] = True` for `i in [iL, iR-1]`.

> Because we included all vertex coordinates in `xs` and `ys`, polygon edges always lie **on cell boundaries**, so each cell is either completely inside or completely outside.

### Step 3: 2D prefix sum over the inside-grid

Build a prefix sum `pref` over `inside` (as 1/0).
This lets us answer in O(1):

> “Are **all cells** inside in the rectangle covering rows `[rowB, rowT)` and columns `[colL, colR)`?”

by checking:

```python
inside_cnt = pref[rowT][colR] - pref[rowB][colR] - pref[rowT][colL] + pref[rowB][colL]
total_cells = (colR - colL) * (rowT - rowB)
rectangle_is_inside = (inside_cnt == total_cells)
```

### Step 4: Try all pairs of red tiles

For each pair of red points `(x1, y1)` and `(x2, y2)`:

* Skip if `x1 == x2` or `y1 == y2` (no area).
* Compute their compressed indices:

```python
colL = min(map_x[x1], map_x[x2])
colR = max(map_x[x1], map_x[x2])
rowB = min(map_y[y1], map_y[y2])
rowT = max(map_y[y1], map_y[y2])
```

* Use the prefix sum to check if the whole continuous rectangle `[xs[colL], xs[colR]] × [ys[rowB], ys[rowT]]` is inside the polygon.
* If yes, its **tile area** is exactly your part 1 formula:

```python
area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
```

Track the maximum.

Complexity:

* Building the inside-grid: ~O(N_rows * N_vertical_edges log N_vertical_edges). With ~500 vertices this is tiny.
* Pair loop: ~N²/2 = ~120k pairs for your input – trivial.

# Day 10:
Gaussian elimination with GF(2)
Integer Linear Programming
* Solve: minimize sum(x) s.t. A x = b, x integer >= 0
* using scipy.optimize.milp (HiGHS).
* Returns minimal total presses (int), or None if infeasible.
https://chatgpt.com/share/695c9146-5d0c-8002-aca1-909c4a75353b

# Day 11:
directed acyclic graph by using dynamic programming with memorization.
https://chatgpt.com/share/695d8bc2-7994-8002-a4c6-62dfc03326d0

# Day 12:
                    (occ, packed)
                         |
               pick first empty cell p
                 /   /   |   \    \
           place1 place2 ... placeM block(p)
              |      |            |
           recurse recurse      recurse
1) Parsing (parse_input)
2) Generate orientations (gen_orients)
3) Bitboard representation
4) Packing the counts (pack_counts, get_count, dec_packed)
5) The solver for one region (can_pack)
6) Core recursion dfs(occ, packed) with memo

https://chatgpt.com/share/695da3aa-d1d4-8002-a197-80dd1e977334