def is_inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def bfs(world, begin):
    n, m = len(world[0]), len(world)

    queue = [begin]
    count = 0

    while queue:
        x, y = queue.pop() # pop() for DFS, pop(0) voor BFS
        value = world[y][x]

        if value == 9:
            count += 1
        else:
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = x + dx, y + dy
                if is_inbound(new_x, new_y, n, m) and world[new_y][new_x] == value + 1:
                    queue.append((new_x, new_y))

    return count


def scores(world, trailheads):
    score = 0
    for trailhead in trailheads:
        current_score = bfs(world, trailhead)
        score += current_score
    return score


if __name__ == '__main__':
    world = []
    trailheads = []

    with open("data/advent10.in") as file:
        for row, line in enumerate(file):
            trailheads += [(col, row) for col, value in enumerate(line) if value == '0']
            world.append(list(map(int, line.rstrip())))

    print(scores(world, trailheads))
