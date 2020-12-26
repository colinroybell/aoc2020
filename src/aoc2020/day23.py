import sys


def part_a(string):
    ptr = [-1 for i in range(0, 10)]
    cups = []
    for c in string:
        cups.append(int(c))

    for i in range(0, len(cups) - 1):
        ptr[cups[i]] = cups[i + 1]
    ptr[cups[-1]] = cups[0]

    curr = cups[0]

    for r in range(0, 100):
        n = curr
        p0 = ptr[curr]
        p1 = ptr[p0]
        p2 = ptr[p1]
        ptr[curr] = ptr[p2]
        ptr[p2] = -1
        dest = curr - 1
        if dest == 0:
            dest = 9
        while dest == p0 or dest == p1 or dest == p2:
            dest -= 1
            if dest == 0:
                dest = 9
        ptr[p2] = ptr[dest]
        ptr[dest] = p0
        curr = ptr[curr]
    score = 0
    curr = ptr[1]
    while curr != 1:
        score = score*10 + curr
        curr = ptr[curr]
    return score


def part_b(string):
    ptr = [-1 for i in range(0, 1000001)]
    cups = []
    for c in string:
        cups.append(int(c))

    for i in range(0, len(cups) - 1):
        ptr[cups[i]] = cups[i + 1]
    ptr[cups[-1]] = 10
    for i in range(10, 1000000):
        ptr[i] = i + 1
    ptr[1000000] = cups[0]

    curr = cups[0]

    for r in range(0, 10000000):
        if r % 100000 == 0:
            print(r)
        n = curr
        p0 = ptr[curr]
        p1 = ptr[p0]
        p2 = ptr[p1]
        ptr[curr] = ptr[p2]
        ptr[p2] = -1
        dest = curr - 1
        if dest == 0:
            dest = 1000000
        while dest == p0 or dest == p1 or dest == p2:
            dest -= 1
            if dest == 0:
                dest = 1000000
        ptr[p2] = ptr[dest]
        ptr[dest] = p0
        curr = ptr[curr]
    curr = 1
    return ptr[curr] * ptr[ptr[curr]]


def entry():
    if 'a' in sys.argv:
        print(part_a('469217538'))
    if 'b' in sys.argv:
        print(part_b('469217538'))


if __name__ == "__main__":
    entry()
