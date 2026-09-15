#
# test the code: python graph_builder_2.py < input.txt
# check the time: time python graph_builder_2.py < input.txt

from collections import defaultdict, deque
def parse_input():
    rules = []
    updates = []
    for line in open(0):
        if '|' in line:
            rules.append(tuple(map(int, line.split('|'))))
        elif ',' in line:
            updates.append(tuple(map(int, line.split(','))))
    return rules, updates

def is_correct_order(update, rules):
    for a, b in rules:
        if a in update and b in update and update.index(a) > update.index(b):
            return False
    return True

def find_middle_page(update):
    return update[len(update)//2]

def to_correct_order(update, rules):
    # create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for a, b in rules:
        if a in update and b in update:
            graph[a].append(b)
            in_degree[b] += 1
        if a not in in_degree and a in update:
            in_degree[a] = 0
    
    # Topological sort using Kahn's algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_nodes = []
    while queue:
        node = queue.popleft()
        sorted_nodes.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_nodes

def main():
    rules, updates = parse_input()
    incorrect_updates = [update for update in updates if not is_correct_order(update, rules)]
    middle_incorrect_updates = [find_middle_page(to_correct_order(update,rules)) for update in updates if not is_correct_order(update, rules)]
    #print(middle_incorrect_updates)
    print(sum(middle_incorrect_updates))

if __name__ == '__main__':
    main()