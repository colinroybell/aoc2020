import sys


def read_grid(filename):
    with open(filename) as f:
        grid = f.readlines()
        grid = [x.strip() for x in grid]
    return grid


def count_grid(grid, xstep, ystep):
    count = 0
    x = 0
    y = 0
    width = len(grid[0])
    while y < len(grid):
        if grid[y][x] == '#':
            count += 1
        x = (x + xstep) % width
        y += ystep

    return count


def part_a(filename):
    grid = read_grid(filename)
    return count_grid(grid, 3, 1)


def part_b(filename):
    grid = read_grid(filename)
    return count_grid(grid, 1, 1) * count_grid(grid, 3, 1) * \
        count_grid(grid, 5, 1) * count_grid(grid, 7, 1) * \
        count_grid(grid, 1, 2)


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day03.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day03.txt'))


if __name__ == "__main__":
    entry()
