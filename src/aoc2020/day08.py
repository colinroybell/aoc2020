import sys


class State:
    def __init__(self, program):
        self.acc = 0
        self.pos = 0
        self.program = []
        print(program)
        for line in program:
            line = line.rstrip()
            fields = line.split()
            self.program.append((fields[0], int(fields[1])))
        self.inst_counts = [0] * (len(program) + 1)

    def step(self):
        self.inst_counts[self.pos] += 1
        (command, field) = self.program[self.pos]
        if command == "nop":
            self.pos += 1
        if command == "acc":
            self.acc += field
            self.pos += 1
        if command == "jmp":
            self.pos += field

    def looped(self):
        return (self.inst_counts[self.pos] > 0)

    def done(self):
        return (self.pos == len(self.program))

    def get_acc(self):
        return self.acc


def part_a(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        print(lines)
    program = State(lines)
    while not program.looped():
        program.step()
    return program.get_acc()


def part_b(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    for i in range(0, len(lines)):
        cmd = lines[i][0:3]
        if cmd != 'acc':
            mod_lines = lines[:]
            if cmd == 'jmp':
                mod_lines[i] = 'nop' + mod_lines[i][3:]
            else:
                mod_lines[i] = 'jmp' + mod_lines[i][3:]
            program = State(mod_lines)
            while not program.looped() and not program.done():
                program.step()
            if program.done():
                return program.get_acc()
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day08.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day08.txt'))


if __name__ == "__main__":
    entry()
