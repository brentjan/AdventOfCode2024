from copy import deepcopy


def check_update(update, rules):
    #crules = deepcopy(rules)
    already_printed = set()
    #before = set()

    for page in update:
        for rule_page, should_come_after in rules.items():
            if page in should_come_after and rule_page in already_printed:
                return False
            
        rules.pop(page)
        already_printed.add(page)
        
    return True


def check_updates(updates, rules):
    total_correct = 0
    for update in updates:
        total_correct += check_update(update, rules)
    return total_correct


rules = dict()
updates = []

# Parse input
with open("data/test.in") as file:

    parsing_rules = True
    for line in file:
        parsing_rules = parsing_rules and line != '\n'

        if parsing_rules:
            a, b = line.rstrip().split('|')
            rules.setdefault(int(a), set()).add(int(b))
        elif line != '\n':
            updates.append(
                list(map(int, line.rstrip().split(',')))
            )

print(rules)
print(check_updates(updates, rules))

