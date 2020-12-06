import sys


def group_score_a(lines):
    responses = set()
    for line in lines:
        for char in line:
            responses.add(char)
    return len(responses)


def group_score_b(lines):
    responses = set()
    for char in lines[0]:
        responses.add(char)

    for line in lines:
        r_copy = [r for r in responses]
        for r in r_copy:
            if r not in line:
                responses.remove(r)
    return len(responses)


def group_score(part, lines):
    if part == 'a':
        return group_score_a(lines)
    else:
        return group_score_b(lines)


def both_parts(part, filename):
    group = []
    total = 0
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                total += group_score(part, group)
                group = []
            else:
                group.append(line)
    total += group_score(part, group)
    return total


def part_a(filename):
    return both_parts('a', filename)


def part_b(filename):
    return both_parts('b', filename)


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day06.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day06.txt'))


if __name__ == "__main__":
    entry()
