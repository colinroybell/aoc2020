import sys


def part_a(filename):
    volts = [0]
    with open(filename, 'r') as f:
        for line in f:
            volts.append(int(line))
    volts.sort()
    volts.append(volts[-1] + 3)
    dc = [0] * 4
    for i in range(0, len(volts) - 1):
        diff = volts[i + 1] - volts[i]
        assert(diff > 0 and diff < 4)
        dc[diff] += 1
    return dc[1] * dc[3]


def part_b(filename):
    volts = [0]
    with open(filename, 'r') as f:
        for line in f:
            volts.append(int(line))
    volts.sort()
    volts.append(volts[-1] + 3)
    count = [0] * len(volts)
    count[0] = 1
    for i in range(1, len(volts)):
        j = 1
        while (j <= i and volts[i] - volts[i - j] <= 3):
            count[i] += count[i - j]
            j += 1
    return count[-1]


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day10.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day10.txt'))


if __name__ == "__main__":
    entry()
