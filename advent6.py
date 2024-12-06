DX = {
    '^': 0,
    '>': 1,
    'v': 0,
    '<': -1
}
DY = {
    '^': -1,
    '>': 0,
    'v': 1,
    '<': 0
}
TURN = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}


def is_inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def determine_startpos(world, n, m):
    guard = ['^', '>', '<', 'v']

    for x in range(n):
        for y in range(m):
            if world[y][x] in guard:
                return x, y, world[y][x]
            
    raise AssertionError("No guard in world")


def determine_path(world):
    n, m = len(world[0]), len(world)
    x, y, guard = determine_startpos(world, n, m)
    path = {(x, y)}
    
    x, y = x + DX[guard], y + DY[guard]
    while is_inbound(x, y, n, m):

        # Stumble upon an object: rotate
        lx, ly = x + DX[guard], y + DY[guard]
        if is_inbound(lx, ly, n, m) and world[ly][lx] == '#':
            guard = TURN[guard]

        path.add((x, y))
        x, y = x + DX[guard], y + DY[guard]

    return len(path)


world = []

with open("data/advent6.in") as file:
    for line in file:
        world.append(line.rstrip())

print(determine_path(world))
