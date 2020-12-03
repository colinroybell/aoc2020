import sys
import re


def part_a(filename):
    pw_re = re.compile(r'(\d+)-(\d+) (.):\ (.+)')
    valid = 0
    with open(filename, 'r') as f:
        for line in f:
            line.rstrip()
            m = pw_re.match(line)
            assert(m)
            min_ = int(m.group(1))
            max_ = int(m.group(2))
            char = m.group(3)
            pw = m.group(4)
            count = pw.count(char)
            if count >= min_ and count <= max_:
                valid += 1
    return valid


def part_b(filename):
    pw_re = re.compile(r'(\d+)-(\d+) (.):\ (.+)')
    valid = 0
    with open(filename, 'r') as f:
        for line in f:
            line.rstrip()
            m = pw_re.match(line)
            assert(m)
            pos1 = int(m.group(1)) - 1
            pos2 = int(m.group(2)) - 1
            char = m.group(3)
            pw = m.group(4)
            if (pw[pos1] == char) ^ (pw[pos2] == char):
                valid += 1

    return valid


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day02.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day02.txt'))


if __name__ == "__main__":
    entry()
