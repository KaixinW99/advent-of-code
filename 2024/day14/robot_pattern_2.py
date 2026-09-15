#
# test the code: python robot_pattern_2.py < input.txt
# check the time: time python robot_pattern_2.py < input.txt

import re
def parse_input():
    robots = []
    for line in open(0):
        x, y, vx, vy = map(int,re.findall(r'-?\d+', line))
        robots.append((x, y, vx, vy))
    return robots

def simulate(robots, row, col):
    new_robots = []
    for x, y, vx, vy in robots:
        nx, ny = (x + vx)%col, (y + vy)%row
        new_robots.append((nx, ny, vx, vy))
    return new_robots

def display(positions, row, col):
    for y in range(row):
        for x in range(col):
            if (x, y) in positions:
                print('#', end='')
            else:
                print('.', end='')
        print()

def nearest_neighbor_distribution(robots, row, col):
    neighbor = 0
    positions = set((x, y) for x, y, _, _ in robots)
    for x, y in positions:
        neighbor_list = [((x+1)%col, y), ((x-1)%col, y), (x, (y+1)%row), (x, (y-1)%row), 
                         ((x+1)%col, (y+1)%row), ((x-1)%col, (y-1)%row), ((x+1)%col, (y-1)%row), ((x-1)%col, (y+1)%row)]
        for nx, ny in neighbor_list:
            if (nx, ny) in positions:
                neighbor += 1
    return neighbor/len(robots)

def main():
    runs = 10000
    row, col = 103, 101
    max_neighbor = [0,0]
    xmax_display = None
    robots = parse_input()
    for i in range(runs):
        robots = simulate(robots, row, col)
        neighbor_distributions = nearest_neighbor_distribution(robots, row, col)
        if max_neighbor[1] < neighbor_distributions:
            max_neighbor = [i+1, neighbor_distributions]
            xmax_display = set((x, y) for x, y, _, _ in robots)
    print("Step: %d, Average_Neighbors: %.3f"%(max_neighbor[0], max_neighbor[1]))
    display(xmax_display, row, col)

if __name__ == '__main__':
    main()