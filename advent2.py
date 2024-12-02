# https://adventofcode.com/2024/day/2


def check_result(result, ascending=True):
    i = 0
    n = len(result)

    bad_results = 0
    safe = True

    while i < n - 1 and safe:
        ok = result[i] < result[i+1] if ascending else result[i] > result[i+1]
        ok = ok and 1 <= abs(result[i] - result[i+1]) <= 3

        if not ok:
            #bad_results += 1
            safe = False

        #safe = bad_results < 2
        i += 1

    return safe


def check_result_for_one_shorted(result):
    i = 0
    safe = False

    while i < len(result) and not safe:
        one_shorted = result[:i] + result[i+1:]

        is_current_safe = check_result(one_shorted)
        if not is_current_safe:
            is_current_safe = check_result(one_shorted, ascending=False)

        safe = is_current_safe
        i += 1

    return safe


total_safe = 0
with open("advent2.in") as file:
    for line in file:
        result = [int(number) for number in line.split(' ')]

        total_safe += check_result_for_one_shorted(result)

print(total_safe)


#print(check_result_for_one_shorted([1, 2, 7, 8, 9]))
