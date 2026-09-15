#
# test the code: python3.10 workflow_class_1.py < input.txt
# check the time: time python3.10 workflow_class_1.py < input.txt

a, _ = open(0).read().split("\n\n")

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
    def count(self, part, workflows):
        #! an instance method that takes in itself
        #* to count the workflow
        total = 0
        for rule in self.rules:
            t_part, f_part = rule.separator(part)
            if t_part is not None:
                total += self.send(t_part, workflows, rule.target)
            if f_part is not None:
                part = f_part
            else:
                break
        else:
            total += self.send(part, workflows, self.default)
        return total
    
    def send(self, part, workflows, target):
        #* send the part to another workflow
        if target == "R":
            return 0
        if target == "A":
            total = 1
            for rs, re in part.values():
                total *= re - rs + 1
            return total
        return workflows[target].count(part, workflows)


class Rule:
    def __init__(self, separator, target) -> None:
        self.separator = separator
        self.target = target
    
    @staticmethod
    def construct(s, rule_factory):
        #! instead of an instance passing to itself
        #! be a class function and call it on the class
        separator, target = s.split(":")
        return Rule(rule_factory(separator), target)

workflows = {}

def rule_factory(s):
    # similar to eval()
    #! Here s serves as the predicate
    #! Predicate is another function with the variable part
    key = s[0]
    cmp = s[1]
    num = int(s[2:])
    
    def inner(part):
        #! help to separate the number range into Ture and False part compared to the cmp.
        #* here part is the number range
        if cmp == "<":
            T = (part[key][0], min(part[key][1], num - 1))
            F = (max(num, part[key][0]), part[key][1])
        elif cmp == ">":
            T = (max(num + 1, part[key][0]), part[key][1])
            F = (part[key][0], min(part[key][1], num))
        else:
            assert False
        
        if T[0] <= T[1]:
            t_part = dict(part)
            t_part[key] = T
        else:
            t_part = None

        if F[0] <= F[1]:
            f_part = dict(part)
            f_part[key] = F
        else:
            f_part = None
        
        return (t_part, f_part)
    
    return inner

for line in a.splitlines():
    name, rest = line[:-1].split("{")
    workflows[name] = Workflow.construct(rest, rule_factory)

#print(workflows["px"].default)
#print(workflows["px"].rules)
#print(workflows["px"].rules[0].predicate)
#print(workflows["px"].rules[0].target)

print(workflows["in"].count({k: (1, 4000) for k in "xmas"}, workflows))

