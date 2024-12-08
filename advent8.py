def is_inbound(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def extrapolate(x, y, dx, dy, rico, n, m, next_formula):
    antinodes = set()
    next_x, next_y = next_formula(x, y, dx, dy, rico, 1)
    distance = 1

    while is_inbound(next_x, next_y, n, m):
        antinodes.add((next_x, next_y))
        distance += 1
        next_x, next_y = next_formula(x, y, dx, dy, rico, distance)

    return antinodes


def determine_antinodes(locations, n, m):
    # Assume locations are ordered top to bottom (correct if parsed and added to locations array that way)
    antinodes = set(locations)

    for i in range(len(locations)-1):
        other_locations = locations[i+1:]
        cx, cy = locations[i]

        for ox, oy in other_locations:
            # Compute antinodes between these two locations
            dx, dy = abs(cx - ox), abs(cy - oy)
            rico = -((oy - cy) / (ox - cx)) # -1 because of our coordinate system in arrays

            # Normalise
            if rico < 0:
                rico = -1
            elif rico > 0:
                rico = 1

            # Extrapolate
            antinodes = antinodes.union(
                extrapolate(cx, cy, dx, dy, rico, n, m, lambda x, y, dx, dy, rico, distance: (x+rico*distance*dx, y-distance*dy))
            )
            antinodes = antinodes.union(
                extrapolate(cx, cy, dx, dy, rico, n, m, lambda x, y, dx, dy, rico, distance: (x-rico*distance*dx, y+distance*dy))
            )
    
    return antinodes


def compute_result(antennas, n, m):
    antinodes = set()
    for antenna, locations in antennas.items():
        antinodes = antinodes.union(determine_antinodes(locations, n, m))

    return antinodes, len(antinodes)


if __name__ == "__main__":
    antennas = dict()
    with open("data/advent8.in") as file:

        nrows, ncols = 0, 0
        for y, line in enumerate(file):
            nrows += 1
            ncols = len(line.rstrip())
            for x, element in enumerate(line.rstrip()):
                if element not in ['.', '#']:
                    antennas.setdefault(element, []).append((x, y))

    antinodes, n = compute_result(antennas, nrows, ncols)
    print(n)
