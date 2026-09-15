'''
=======================================================================
ADVENT OF CODE 2022 - Day 12: Hill Climbing Algorithm
=======================================================================
'''
import time
from collections import defaultdict, deque

#Timing: Star
start = time.perf_counter()

#Load the data
file = open("input.dat", 'r')
input = [line.strip() for line in file.readlines()]
max_row, max_col = len(input), len(input[0])


#Parse the data
def text_to_grid(text_line: list):
  grid_map = defaultdict(int)
  for x, line in enumerate(text_line):
    for y, number in enumerate(line):
      grid_map[(x, y)] = int(ord(number))
  return grid_map


#Body
class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y


class queueNode:

  def __init__(self, pt, dist):
    self.pt = pt
    self.dist = dist

  def __str__(self) -> str:
    return f"{self.pt.x};{self.pt.y},{self.dist}"


def find_S_and_E(grid_map):
  src = None
  end = None
  for key, value in grid_map.items():
    if value == ord("S"):
      grid_map[key] = ord("a")
      src = key
    elif value == ord("E"):
      grid_map[key] = ord("z")
      end = key
  return src, end


def is_in_grid(row, col):
  return (row >= 0) and (row < max_row) and (col >= 0) and (col < max_col)


def move_to_next_cell(grid, curr_letter, row, col):
  next_letter = grid[(row, col)]
  return (next_letter == curr_letter + 1) or (next_letter <= curr_letter)


def breath_first_search(grid, src, end):
  rowMove = [-1, 0, 0, 1]
  colMove = [0, -1, 1, 0]

  visited = [[False for _ in range(max_col)] for _ in range(max_row)]
  visited[src.x][src.y] = True

  q = deque()
  qN = queueNode(src, 0)
  q.append(qN)

  while q:
    curr = q.popleft()
    pt = curr.pt

    if pt.x == end.x and pt.y == end.y:
      return curr.dist

    for i in range(4):
      row = pt.x + rowMove[i]
      col = pt.y + colMove[i]

      if (is_in_grid(row, col)
          and move_to_next_cell(grid, grid[(pt.x, pt.y)], row, col)
          and not visited[row][col]):

        visited[row][col] = True
        q.append(queueNode(Point(row, col), curr.dist + 1))

  return -1 #Can't reache the destination


#Main
grid_map = text_to_grid(input)
src, end = find_S_and_E(grid_map)

S = Point(src[0], src[1])
E = Point(end[0], end[1])

print("Part 1 answer : ", breath_first_search(grid_map, S, E))


def get_all_a(grid_map):
  coord = []
  for key, value in grid_map.items():
    if grid_map[key] == ord("a"):
      coord.append(key)
  return coord


dists = [
  breath_first_search(grid_map, Point(a[0], a[1]), E)
  for a in get_all_a(grid_map)
  if breath_first_search(grid_map, Point(a[0], a[1]), E) != -1
]

print("Part 2 answer : ", min(dists))

#Timing: End
end = time.perf_counter()
print(f"\nTime to complete = {(end-start)*1000:.2f} milliseconds.")
