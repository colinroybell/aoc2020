import sys


def part_a(filename):
    deck = [[], []]
    player = -1
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                continue
            elif line[0] == 'P':
                player += 1
            else:
                deck[player].append(int(line))

    round = 1
    while (len(deck[0]) > 0 and len(deck[1]) > 0):
        c0 = deck[0].pop(0)
        c1 = deck[1].pop(0)

        if c0 > c1:
            deck[0].append(c0)
            deck[0].append(c1)
        else:
            deck[1].append(c1)
            deck[1].append(c0)

        round += 1

    if (len(deck[0]) > 0):
        w = 0
    else:
        w = 1

    mult = 1
    score = 0
    while (len(deck[w])):
        v = deck[w].pop(-1)
        score += v * mult
        mult += 1

    return score


def game(deck):
    configurations = set()
    round = 1
    while (len(deck[0]) > 0 and len(deck[1]) > 0):
        config = tuple([tuple(deck[0]), tuple(deck[1])])
        c0 = deck[0].pop(0)
        c1 = deck[1].pop(0)

        if config in configurations:
            deck[0].append(c0)
            deck[0].append(c1)
            return (0, deck)

        configurations.add(config)

        if (len(deck[0]) >= c0 and len(deck[1]) >= c1):
            w, _ = game([deck[0][0:c0], deck[1][0:c1]])
        else:
            if c0 > c1:
                w = 0
            else:
                w = 1

        if w == 0:
            deck[0].append(c0)
            deck[0].append(c1)
        else:
            deck[1].append(c1)
            deck[1].append(c0)

        round += 1

    if (len(deck[0]) > 0):
        w = 0
    else:
        w = 1
    return (w, deck)


def part_b(filename):
    configurations = set()
    deck = [[], []]
    player = -1
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                continue
            elif line[0] == 'P':
                player += 1
            else:
                deck[player].append(int(line))

    (w, deck) = game(deck)

    mult = 1
    score = 0
    while (len(deck[w])):
        v = deck[w].pop(-1)
        score += v * mult
        mult += 1
    return score


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day22.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day22.txt'))


if __name__ == "__main__":
    entry()
