import sys


def move(pos, dir):
    (x, y) = pos
    if dir == 'e':
        return (x + 1, y)
    elif dir == 'w':
        return (x - 1, y)
    elif dir == 'ne':
        return (x, y + 1)
    elif dir == 'sw':
        return (x, y - 1)
    elif dir == 'se':
        return (x + 1, y - 1)
    elif dir == 'nw':
        return (x - 1, y + 1)


def count_black(loc):
    total = 0
    for pos in loc:
        total += loc[pos]
    return total


def both_parts(filename, part):
    loc = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            pos = (0, 0)
            inst = ""
            for c in line:
                inst = inst + c
                if c == 'e' or c == 'w':
                    pos = move(pos, inst)
                    inst = ""
            if pos not in loc:
                loc[pos] = 0
            loc[pos] = 1 - loc[pos]

    if part == 'a':
        return count_black(loc)

    else:
        dirs = ['e', 'w', 'se', 'nw', 'sw', 'ne']
        print(loc)
        for round in range(0, 100):
            count = {}
            for pos, c in loc.items():
                if c == 0:
                    continue
                if pos not in count:
                    # Mark current in case we have no adjacents
                    count[pos] = 0
                for dir in dirs:
                    adj = move(pos, dir)
                    if adj not in count:
                        count[adj] = 0
                    count[adj] += 1

            for pos, c in count.items():
                col = 0
                if pos in loc and loc[pos] == 1:
                    col = 1
                if col == 0 and c == 2:
                    loc[pos] = 1
                if col == 1 and (c == 0 or c > 2):
                    loc[pos] = 0
        return count_black(loc)


def part_a(filename):
    return both_parts(filename, 'a')


def part_b(filename):
    return both_parts(filename, 'b')


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day24.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day24.txt'))


if __name__ == "__main__":
    entry()
