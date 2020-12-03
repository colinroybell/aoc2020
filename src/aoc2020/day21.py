import sys


def part_a(filename):
    return 0


def part_b(filename):
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day21.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day21.txt'))


if __name__ == "__main__":
    entry()