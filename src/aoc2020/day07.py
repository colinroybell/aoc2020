import sys


def parse_file(filename):
    down = {}
    up = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            fields = line.split()
            bag = fields[0] + ' ' + fields[1]
            pos = 4
            down[bag] = []
            while (pos + 3) < len(fields):
                count = int(fields[pos])
                subbag = fields[pos+1] + ' ' + fields[pos+2]
                if bag in down:
                    down[bag].append((count, subbag))
                else:
                    down[bag] = [(count, subbag)]
                if bag not in up:
                    up[bag] = []
                if subbag in up:
                    up[subbag].append((count, bag))
                else:
                    up[subbag] = [(count, bag)]
                pos += 4
    return (down, up)


def compute_holders(up, bag):
    holders = set()
    holders.add(bag)
    for (count, superbag) in up[bag]:
        ret = compute_holders(up, superbag)
        holders = holders.union(ret)
    return holders


# note: caching the answers would be more efficient, but for our
# case it runs more or less instantly anyway
def compute_held(down, bag):
    total = 1
    for (count, subbag) in down[bag]:
        total += count * compute_held(down, subbag)
    return total


def part_a(filename):
    (down, up) = parse_file(filename)
    holders = compute_holders(up, 'shiny gold')
    return len(holders) - 1


def part_b(filename):
    (down, up) = parse_file(filename)
    held = compute_held(down, 'shiny gold')
    return held - 1


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day07.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day07.txt'))


if __name__ == "__main__":
    entry()
