import sys


def seat_id(code):
    row = 0
    for i in range(0, 7):
        row *= 2
        if code[i] == 'B':
            row += 1
    col = 0
    for i in range(7, 10):
        col *= 2
        if code[i] == 'R':
            col += 1
    return row * 8 + col


def part_a(filename):
    max_id = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            id = seat_id(line)
            max_id = max(max_id, id)
    return max_id


def part_b(filename):
    ids = set()
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            id = seat_id(line)
            ids.add(id)

    for seat in ids:
        if (seat + 2) in ids and not (seat + 1) in ids:
            return seat + 1
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day05.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day05.txt'))


if __name__ == "__main__":
    entry()
