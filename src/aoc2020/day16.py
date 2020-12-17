import sys
import re


def part_a(filename):
    ranges = []
    state = 1
    count = 1
    total = 0
    range_re = re.compile(r': (\d+)-(\d+) or (\d+)-(\d+)')
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                state += 1
                count = 0
            elif state == 1:
                m = range_re.search(line)
                assert(m)
                ranges.append((int(m.group(1)), int(m.group(2))))
                ranges.append((int(m.group(3)), int(m.group(4))))
            elif state == 2:
                pass
            elif state == 3:
                count += 1
                if count == 1:
                    continue
                strings = line.split(',')
                for s in strings:
                    v = int(s)
                    ok = False
                    for r in ranges:
                        if v >= r[0] and v <= r[1]:
                            ok = True
                    if not ok:
                        total += v
    return total


def part_b(filename):
    fields = []
    ranges = []
    your_ticket = []
    tickets = []
    state = 1
    count = 1
    total = 0
    range_re = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == '':
                state += 1
                count = 0
            elif state == 1:
                m = range_re.search(line)
                assert(m)
                r1 = (int(m.group(2)), int(m.group(3)))
                r2 = (int(m.group(4)), int(m.group(5)))
                fields.append((m.group(1), r1, r2))
                ranges.append((int(m.group(2)), int(m.group(3))))
                ranges.append((int(m.group(4)), int(m.group(5))))
            elif state == 2:
                count += 1
                if count == 2:
                    strings = line.split(',')
                    for s in strings:
                        v = int(s)
                        your_ticket.append(v)
            elif state == 3:
                count += 1
                if count == 1:
                    continue
                strings = line.split(',')
                ticket = []
                ticket_ok = True
                for s in strings:
                    v = int(s)

                    ticket.append(v)
                    ok = False
                    for r in ranges:
                        if v >= r[0] and v <= r[1]:
                            ok = True
                    if not ok:
                        ticket_ok = False
                        break

                if ticket_ok:
                    tickets.append(ticket)

    size = len(fields)

    b = [[0 for i in range(0, size)] for j in range(0, size)]

    for row, f in enumerate(fields):
        for col in range(0, size):
            ok = True
            for t in tickets:
                v = t[col]
                if not ((v >= f[1][0] and v <= f[1][1]) or
                        (v >= f[2][0] and v <= f[2][1])):
                    ok = False
                    break
            if ok:
                b[row][col] = 1

    sigma = 0
    while sigma != size:
        sigma = 0
        for r in range(0, size):
            count = 0
            loc = 0
            for c in range(0, size):
                count += b[r][c]
                if b[r][c]:
                    loc = c
            if count == 1:
                for r2 in range(0, size):
                    if r != r2:
                        b[r2][loc] = 0

        for c in range(0, size):
            count = 0
            loc = 0
            for r in range(0, size):
                count += b[r][c]
                if b[r][c]:
                    loc = r
            if count == 1:
                for c2 in range(0, size):
                    if c != c2:
                        b[loc][c2] = 0
            sigma += count

    prod = 1
    for i in range(0, size):
        if fields[i][0][0:9] == 'departure':
            loc = 0
            for c in range(0, size):
                if b[i][c]:
                    loc = c
            prod *= your_ticket[loc]
    return prod


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day16.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day16.txt'))


if __name__ == "__main__":
    entry()
