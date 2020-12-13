import sys


def part_a(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        base = int(line)
        line = f.readline()
        intervals = line.split(',')
        earliest = 1e6 * base
        score = 0
        for interval in intervals:
            if interval == 'x':
                continue
            t = int(interval)
            time = t * ((base + t - 1) // t)
            if time < earliest:
                earliest = time
                score = (time - base) * t
    return score


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def part_b(filename):
    with open(filename, 'r') as f:
        line = f.readline()
        # ignore first line
        line = f.readline()
        intervals = line.split(',')
        t = 0
        div = 1
        constraints = []
        for i, string in enumerate(intervals):
            if string == 'x':
                continue
            interval = int(string)
            constraints.append((interval, i))
            while (t % interval != (interval - i) % interval):
                t += div
            div = lcm(div, interval)
            for j in constraints:
                assert(t % j[0] == (j[0] - j[1]) % j[0])
    return t


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day13.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day13.txt'))


if __name__ == "__main__":
    entry()
