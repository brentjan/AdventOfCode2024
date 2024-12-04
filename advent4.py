def is_inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def x_mas(x, y, lines, n, m):
    if not (0 < x < n - 1 and 0 < y < m - 1):
        return 0
    
    diagonal_1 = lines[x-1][y-1] + lines[x][y] + lines[x+1][y+1]
    diagonal_2 = lines[x-1][y+1] + lines[x][y] + lines[x+1][y-1]

    if diagonal_1 in ['MAS', 'SAM'] and diagonal_2 in ['MAS', 'SAM']:
        return 1
    else:
        return 0
            

name = "data/advent4.in"
total = 0

with open(name) as file:
    lines = [line.rstrip() for line in file]
    n, m = len(lines[0]), len(lines)

    for y in range(m):
        for x in range(n):
            total += x_mas(x, y, lines, n, m)

print(total)


# def xmas(x, y, lines, n, m):
#     strings = []
#     for dx in [-1, 0, 1]:
#         for dy in [-1, 0, 1]:
#             if dx != 0 or dy != 0:
#                 string = lines[x][y]
#                 for factor in range(1, 4):

#                     new_x, new_y = x+dx*factor, y+dy*factor
#                     string += lines[new_x][new_y] if is_inbound(new_x, new_y, n, m) else ""
                
#                 if len(string) == 4:
#                     strings.append(string)

#     return sum([string == 'XMAS' for string in strings])
