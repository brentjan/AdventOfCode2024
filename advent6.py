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
    for x in range(n):
        for y in range(m):
            if world[y][x] in ['^', '>', '<', 'v']:
                return x, y, world[y][x]
            
    raise AssertionError("No guard in world")


def determine_path(world, n, m, obstruction=None):
    x, y, guard = determine_startpos(world, n, m)
    path = dict()

    while path.get((x, y, guard), 0) < 2 and is_inbound(x, y, n, m):

        new_x, new_y = x + DX[guard], y + DY[guard]
        if (new_x, new_y) == obstruction or (is_inbound(new_x, new_y, n, m) and world[new_y][new_x] == '#'):
            guard = TURN[guard]
            new_x, new_y = x + DX[guard], y + DY[guard]

        path[(x, y, guard)] = path.get((x, y, guard), 0) + 1
        x, y = new_x, new_y

    return path, is_inbound(x, y, n, m) # True if cycle


def determine_cycles(world):
    n, m = len(world[0]), len(world)
    x, y, _ = determine_startpos(world, n, m)

    path, _ = determine_path(world, n, m)

    obstructions = 0

    xs_ys = {(x, y) for x in range(n) for y in range(m)} \
        .intersection({(x, y) for (x, y, _) in path.keys()}) \
        .difference({(x, y)})
    
    for x, y in xs_ys:
        if world[y][x] != '#': # If there's already an obstruction: do nothing
            _, cycle = determine_path(world, n, m, (x, y))

            if cycle:
                obstructions += 1

    return obstructions


world = []
with open("data/advent6.in") as file:
    for line in file:
        world.append(line.rstrip())

print(determine_cycles(world))
