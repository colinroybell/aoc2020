import sys


def iterate(grid):
    counts = {}
    for v in grid:
        (x, y, z) = v
        for xs in range(-1, 2):
            for ys in range(-1, 2):
                for zs in range(-1, 2):
                    if xs != 0 or ys != 0 or zs != 0:
                        adj = (x + xs, y + ys, z + zs)
                        if adj in counts:
                            counts[adj] += 1
                        else:
                            counts[adj] = 1
    new_grid = set()
    for (v, c) in counts.items():
        if c == 3 or (c == 2 and v in grid):
            new_grid.add(v)
    return new_grid


def iterate4(grid):
    counts = {}
    for v in grid:
        (x, y, z, w) = v
        for xs in range(-1, 2):
            for ys in range(-1, 2):
                for zs in range(-1, 2):
                    for ws in range(-1, 2):
                        if xs != 0 or ys != 0 or zs != 0 or ws != 0:
                            adj = (x + xs, y + ys, z + zs, w + ws)
                            if adj in counts:
                                counts[adj] += 1
                            else:
                                counts[adj] = 1
    new_grid = set()
    for (v, c) in counts.items():
        if c == 3 or (c == 2 and v in grid):
            new_grid.add(v)
    return new_grid


def part_a(filename):
    grid = set()
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            x = 0
            for c in line:
                if c == '#':
                    grid.add((x, y, 0))
                x += 1
            y += 1

    for i in range(0, 6):
        grid = iterate(grid)
    return len(grid)


def part_b(filename):
    grid = set()
    with open(filename, 'r') as f:
        y = 0
        for line in f:
            x = 0
            for c in line:
                if c == '#':
                    grid.add((x, y, 0, 0))
                x += 1
            y += 1

    for i in range(0, 6):
        grid = iterate4(grid)
    return len(grid)


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day17.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day17.txt'))


if __name__ == "__main__":
    entry()
