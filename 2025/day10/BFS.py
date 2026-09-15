#! /usr/bin/env python3
import sys
from collections import deque
def BFS(target, buttons):
    initial_state = list(0 for _ in target)
    queue = deque([(0, initial_state)])  #(steps, initial_state)
    while queue:
        steps, state = queue.popleft()
        if state == target:
            return steps
        for button in buttons:
            new_state = state[:]
            for i in button:
                new_state[i] = 1 - new_state[i]  # toggle light
            queue.append((steps + 1, new_state))
    return ValueError("No solution found")

total_fewest_button_presses = 0
for i, line in enumerate(sys.stdin):
    if line.strip() == "":
        continue
    ind_light, *buttons, _ = line.split()
    ind_light = list(0 if light=='.' else 1 for light in ind_light.strip("[]"))
    buttons = [list(map(int, b.strip("()").split(","))) for b in buttons]
    fewest_button_presses = BFS(ind_light, buttons)
    #print(f"Case {i+1}: {fewest_button_presses}")
    total_fewest_button_presses += fewest_button_presses
print(total_fewest_button_presses)