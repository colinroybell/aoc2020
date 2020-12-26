import sys


rules = {}


class Rule:
    def __init__(self, n, letter, subrules):
        self.n = n
        self.letter = letter
        self.subrules = subrules
        self.initialised = False

    def setup(self, part):
        if part == 'b' and (self.n == 0 or self.n == 8 or self.n == 11):
            return set()
        if self.initialised:
            return self.list
        elif self.letter:
            self.list = set([self.letter])
        else:
            self.list = set()
            for sr in self.subrules:
                first = True
                for r in sr:
                    if first:
                        ok = rules[r].setup(part)
                        first = False
                    else:
                        ok_sub = rules[r].setup(part)
                        new_ok = set()
                        for m in ok:
                            for n in ok_sub:
                                new_ok.add(m + n)
                        ok = new_ok
                self.list = self.list.union(ok)
        self.initialised = True
        return self.list


def part_a(filename):
    status = 1
    test_lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                status += 1
            elif status == 1:
                f1 = line.split(': ')
                n = int(f1[0])
                letter = ""
                lists = []
                if f1[1][0] == '"':
                    letter = f1[1][1]
                else:
                    f2 = f1[1].split(' ')
                    lists = []
                    subrule = []
                    for i in f2:
                        if i == '|':
                            lists.append(subrule)
                            subrule = []
                        else:
                            subrule.append(int(i))
                    lists.append(subrule)
                rules[n] = Rule(n, letter, lists)
            else:
                test_lines.append(line)

    passing = rules[0].setup('a')
    count = 0
    for line in test_lines:
        if line in passing:
            count += 1
    return count


def part_a(filename):
    status = 1
    test_lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                status += 1
            elif status == 1:
                f1 = line.split(': ')
                n = int(f1[0])
                letter = ""
                lists = []
                if f1[1][0] == '"':
                    letter = f1[1][1]
                else:
                    f2 = f1[1].split(' ')
                    lists = []
                    subrule = []
                    for i in f2:
                        if i == '|':
                            lists.append(subrule)
                            subrule = []
                        else:
                            subrule.append(int(i))
                    lists.append(subrule)
                rules[n] = Rule(n, letter, lists)
            else:
                test_lines.append(line)

    passing = rules[0].setup('a')
    count = 0
    for line in test_lines:
        if line in passing:
            count += 1
    return count


def trial(line, state, m, n, subs):
    if state == 0:
        list_42 = rules[42].setup('b')
        # need to check at least one character, and leave one left for 31
        for c in range(1, len(line)):
            if line[0:c] in list_42:
                if trial(line[c:], 0, m + 1, n, subs + [line[0:c]]):
                    return True
    state = 1
    list_31 = rules[31].setup('b')
    if n >= m - 1 or m < 2:
        return False
    if line in list_31 and n < m:
        return True
    for c in range(1, len(line)):
        if line[0:c] in list_31:
            if trial(line[c:], 1, m, n + 1, subs + [line[0:c]]):
                return True
    return False


def part_b(filename):
    status = 1
    test_lines = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                status += 1
            elif status == 1:
                f1 = line.split(': ')
                n = int(f1[0])
                letter = ""
                lists = []
                if f1[1][0] == '"':
                    letter = f1[1][1]
                else:
                    f2 = f1[1].split(' ')
                    lists = []
                    subrule = []
                    for i in f2:
                        if i == '|':
                            lists.append(subrule)
                            subrule = []
                        else:
                            subrule.append(int(i))
                    lists.append(subrule)
                rules[n] = Rule(n, letter, lists)
            else:
                test_lines.append(line)

    passing = rules[0].setup('b')
    # The effect of what we have is that we need things to be M 42s + N 31s,
    # with M > N and N>=1
    count = 0
    for line in test_lines:
        ok = trial(line, 0, 0, 0, [])
        if ok:
            count += 1
    return count


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day19.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day19.txt'))


if __name__ == "__main__":
    entry()
