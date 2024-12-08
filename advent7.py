def branch_and_bound(result, accumulator, leftover_operands):
    if len(leftover_operands) == 0 or accumulator > result:
        return accumulator == result
    else:
        # Try +
        accumulator_plus = accumulator + leftover_operands[0]
        if not accumulator_plus > result:
            plus_result = branch_and_bound(result, accumulator_plus, leftover_operands[1:])
        else:
            plus_result = False

        # Try *
        accumulator_mul = accumulator * leftover_operands[0]
        if not accumulator_mul > result:
            mul_result = branch_and_bound(result, accumulator_mul, leftover_operands[1:])
        else:
            mul_result = False

        # Try || (part 2)
        accmulator_concat = int(str(accumulator) + str(leftover_operands[0]))
        if not accmulator_concat > result:
            concat_result = branch_and_bound(result, accmulator_concat, leftover_operands[1:])
        else:
            concat_result = False

        return plus_result or mul_result or concat_result


def determine_operator(result, operands): 
    return branch_and_bound(result, operands[0], operands[1:])


def determine_operators(tests):
    summation = 0
    for result, operands in tests:
        is_possible = determine_operator(result, operands)

        if is_possible:
            summation += result

    return summation


tests = []
with open("data/advent7.in") as file:
    for line in file:
        line = line.rstrip().split(':')

        result = int(line[0])
        operands = [int(operand) for operand in line[1].split(' ')[1:]]
        tests.append((result, operands))

print(determine_operators(tests))
