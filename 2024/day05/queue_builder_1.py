#
# test the code: python queue_builder_1.py < input.txt
# check the time: time python queue_builder_1.py < input.txt
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

def main():
    rules, updates = parse_input()
    middle_correct_updates = [find_middle_page(update) for update in updates if is_correct_order(update, rules)]
    #print(middle_correct_updates)
    print(sum(middle_correct_updates))

if __name__ == '__main__':
    main()