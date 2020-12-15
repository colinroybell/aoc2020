import sys


def run(filename, length):
    starting = []
    spoken = []
    last = {}
    with open(filename, 'r') as f:
        line = f.readline()
        line = line.rstrip()
        n = line.split(',')
        for k in n:
            starting.append(int(k))
    for r in range(0, length):
        if r < len(starting):
            num = starting[r]
        else:
            if spoken[-1] in last:
                num = r - last[spoken[-1]] - 1
            else:
                num = 0
        if r > 0:
            last[spoken[-1]] = r-1
        spoken.append(num)

    return spoken[-1]


def part_a(filename):
    return run(filename, 2020)


def part_b(filename):
    return run(filename, 30000000)


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day15.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day15.txt'))


if __name__ == "__main__":
    entry()
