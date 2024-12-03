import re

result = 0
with open("data/advent3.in") as file:
    memory = "".join(file)
    do = True

    for match in re.finditer("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", memory):
        instruction = match.group()

        if instruction == 'do()':
            do = True
        elif instruction == "don't()":
            do = False
        elif do:
            a, b = re.match("mul\(([0-9]+),([0-9]+)\)", instruction).groups()
            result += int(a) * int(b)

print(result)
