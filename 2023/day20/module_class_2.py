#
# test the code: python3.10 module_class_1.py < input.txt
# check the time: time python3.10 module_class_1.py < input.txt
import math
from collections import deque
class Module:
    def __init__(self, name, type, outputs) -> None:
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            # % type
            self.memory = "off"
        else:
            # & type
            self.memory = {}
    
    def __repr__(self) -> str:
        return self.name + "{type=" + self.type + ",outputs=" + ",".join(self.outputs) + ",memory=" + str(self.memory) + "}"

modules = {}
broadcast_targets = []

for line in open(0):
    left, right = line.strip().split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        broadcast_targets = outputs
    else:
        type = left[0]
        name = left[1:]
        modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "lo"

# assumption 1: there is only one to rx
(feed, ) = [name for name, module in modules.items() if "rx" in module.outputs]

# assumption 2: for others connected to the one with rx, they will have periodic shift
# so we need to obtian the LCM
cycle_lengths = {}
seen = {name: 0 for name, module in modules.items() if feed in module.outputs}

presses = 0

while True:
    presses += 1 
    # origin, target, pulse
    q = deque([("broadcaster", x, "lo") for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()
        
        if target not in modules:
            continue

        module = modules[target]

        if module.name == feed and pulse == "hi":
            seen[origin] += 1

            # to test whether that fit for our assumption 2
            if origin not in cycle_lengths:
                cycle_lengths[origin] = presses
            else:
                assert presses == seen[origin] * cycle_lengths[origin]
            
            # to test whether the code will get stuck at somewhere else
            if all(seen.values()):
                #print(cycle_lengths.values())
                x = 1
                for cycle_length in cycle_lengths.values():
                    x = math.lcm(x, cycle_length)
                    #x *= cycle_length // math.gcd(x, cycle_length)
                print(x)
                exit(0)

        if module.type == "%":
            if pulse == "lo":
                module.memory = "on" if module.memory == "off" else "off"
                outgoing = "hi" if module.memory == "on" else "lo"
                for x in module.outputs:
                    q.append((module.name, x, outgoing))
        else:
            module.memory[origin] = pulse
            outgoing = "lo" if all(x == "hi" for x in module.memory.values()) else "hi"
            for x in module.outputs:
                q.append((module.name, x, outgoing))
