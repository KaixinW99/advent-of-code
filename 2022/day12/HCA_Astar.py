from typing import Protocol, Iterator, Tuple, TypeVar, Optional
T = TypeVar("T") # typing.TypeVar: https://docs.python.org/3/library/typing.html
Location = TypeVar("Location")
class Graph(Protocol): # typing.Protocol: https://docs.python.org/3/library/typing.html
    def neighbors(self,id: Location)->list[Location]: pass

# Grid Graph
GridLocation = Tuple[int,int] # typing.Tuple: https://docs.python.org/3/library/typing.html
class SquareGrid:
    def __init__(self,width:int,height:int) -> None:
        self.width=width
        self.height=height
        self.walls: list[GridLocation]=[]
    def in_bounds(self,id:GridLocation)->bool:
        (x,y)=id
        return (0<=x<self.width) and (0<=y<self.height)
    def passable(self,id:GridLocation)->bool:
        return id not in self.walls
    def neighbors(self,id:GridLocation)->Iterator[GridLocation]: # typing.Iterator: https://docs.python.org/3/library/typing.html
        (x,y)=id
        neighbors = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

# Graph with weights
def WeightedGraph(Graph):
    def cost(self,from_ide:Location,to_id:Location)->float:pass
class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height) # super() in class inheritance: https://realpython.com/python-super/
        self.weights: dict[GridLocation,float]={}
    def cost(self,from_node:GridLocation,to_node:GridLocation)-> float:
        return self.weights.get(from_node,1),self.weights.get(to_node,1)


import heapq # heapq: https://docs.python.org/3/library/heapq.html
class PriorityQueue:
    def __init__(self) -> None:
        self.elements: list[tuple[float,T]]=[]
    def empty(self)->bool:
        return not self.elements
    def put(self,item:T, priority:float):
        heapq.heappush(self.elements,(priority,item))
    def get(self)->T:
        return heapq.heappop(self.elements)[1]

"""
import collections
class Queue:
    def __init__(self) -> None:
        self.elements=collections.deque()
    def empty(self) -> bool:
        return not self.elements
    def put(self, x:T):
        self.elements.append(x)
    def get(self) -> T:
        return self.elements.popleft()

def breadth_first_search(graph:Graph,start:Location,goal:Location):
    frontier=Queue()
    frontier.put(start)
    came_from:dict[Location,Optional[Location]]={} # typing.Optional: https://docs.python.org/3/library/typing.html
    came_from[start]=None
    while not frontier.empty():
        current: Location=frontier.get()
        if current==goal: #early exit
            break
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next]=current
    return came_from
"""

def heuristic(a:GridLocation,b:GridLocation)->float:
    (x1,y1)=a
    (x2,y2)=b
    return abs(x1-x2)+abs(y1-y2)

def a_star_search(graph: WeightedGraph, start: Location, goal: Location):
    frontier = PriorityQueue()
    frontier.put(start,0)
    came_from: dict[Location, Optional[Location]]={}
    step_so_far: dict[Location, float]={}

    came_from[start]=None
    step_so_far[start]=0

    while not frontier.empty():
        current: Location=frontier.get()
        if current==goal:
            break
        for next in graph.neighbors(current):
            new_cost=step_so_far[current]+1
            current_step, next_step = graph.cost(current,next)
            if ((next not in step_so_far) or (new_cost < step_so_far.get(next,float('inf')))) and (next_step-current_step<=1):
                step_so_far[next]=new_cost
                priority = new_cost+heuristic(next,goal)
                frontier.put(next,priority)
                came_from[next]=current
    return came_from, step_so_far

import numpy as np
import sys
#np.set_printoptions(threshold=sys.maxsize)
def convertfunc(x):
    if x=="S":
        return 1
    elif x=="E":
        return 26
    else:
        return ord(str(x))-96

with open("input.dat") as f: l = len(f.readline().strip())
f = np.genfromtxt("input.dat",dtype=str,delimiter=[1 for _ in range(l)])
lr, lc = len(f), l

# ! Part 1
start = tuple(np.argwhere(f=="S")[0])
goal  = tuple(np.argwhere(f=="E")[0])
m = GridWithWeights(lr, lc)
m.weights = {(x,y):convertfunc(f[x,y]) for x in range(lr) for y in range(lc)}
came_from, cost_so_far= a_star_search(m, start, goal)
print("Answer to part 1:",cost_so_far[goal])

# ! Part 2
from tqdm import tqdm
starts = np.argwhere(f=="a") # all the position lists of "a"
goal  = tuple(np.argwhere(f=="E")[0])
m = GridWithWeights(lr, lc)
m.weights = {(x,y):convertfunc(f[x,y]) for x in range(lr) for y in range(lc)}
total_dist = []
for s in tqdm(starts):
    came_from, cost_so_far= a_star_search(m, tuple(s), goal)
    if goal in cost_so_far: # some of the point cannot get to the destination
        total_dist.append(cost_so_far[goal])
print("Answer to part 2:", min(total_dist))