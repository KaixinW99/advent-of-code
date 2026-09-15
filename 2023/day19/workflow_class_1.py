#
# test the code: python3.10 workflow_class_1.py < input.txt
# check the time: time python3.10 workflow_class_1.py < input.txt

a, b = open(0).read().split("\n\n")

class Workflow:
    def __init__(self, rules, default) -> None:
        self.rules = rules
        self.default = default
    
    @staticmethod
    def construct(s, rule_factory):
        #! instead of an instance passing to itself
        #! be a class function and call it on the class
        *rules, default = s.split(",")
        return Workflow([Rule.construct(rule, rule_factory) for rule in rules], default)
    def process(self, part, workflows):
        #! an instance method that takes in itself
        #* to process the workflow
        for rule in self.rules:
            if rule.predicate(part):
                return self.send(part, workflows, rule.target)
        return self.send(part, workflows, self.default)
    
    def send(self, part, workflows, target):
        #* send the part to another workflow
        if target == "R":
            return 0
        if target == "A":
            return sum(part.values())
        return workflows[target].process(part, workflows)


class Rule:
    def __init__(self, predicate, target) -> None:
        self.predicate = predicate
        self.target = target
    
    @staticmethod
    def construct(s, rule_factory):
        #! instead of an instance passing to itself
        #! be a class function and call it on the class
        predicate, target = s.split(":")
        return Rule(rule_factory(predicate), target)

workflows = {}

def rule_factory(s):
    # similar to eval()
    #! Here s serves as the predicate
    #! Predicate is another function with the variable part
    key = s[0]
    cmp = s[1]
    num = int(s[2:])

    if cmp == "<":
        return lambda part: part[key] < num
    if cmp == ">":
        return lambda part: part[key] > num
    
    assert False

for line in a.splitlines():
    name, rest = line[:-1].split("{")
    workflows[name] = Workflow.construct(rest, rule_factory)

#print(workflows["px"].default)
#print(workflows["px"].rules)
#print(workflows["px"].rules[0].predicate)
#print(workflows["px"].rules[0].target)

total = 0

for line in b.splitlines():
    # make a dictionary from the list
    part = {}
    for item in line[1:-1].split(","):
        k, v = item.split("=")
        part[k] = int(v)
    total += workflows["in"].process(part, workflows)

print(total)