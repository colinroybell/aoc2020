import sys


def part_a(filename):
    entry = set()
    with open(filename, 'r') as f:
        for line in f:
            val = int(line)
            entry.add(val)
            inverse = 2020 - val
            if inverse in entry:
                return val * inverse
    return 0


def part_b(filename):
    entry = set()
    pairs = {}
    with open(filename, 'r') as f:
        for line in f:
            val = int(line)
            for e in entry:
                pairs[val + e] = val * e
            entry.add(val)
            inverse = 2020 - val
            if inverse in pairs:
                return val * pairs[inverse]
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day01.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day01.txt'))


if __name__ == "__main__":
    entry()
