for num in range(5, 26):
    n = "{:02d}".format(num)

    main_file = """import sys


def part_a(filename):
    return 0


def part_b(filename):
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day{}.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day{}.txt'))


if __name__ == "__main__":
    entry()
""".format(n, n)

    main_filename = "day{}.py".format(n)
    with open(main_filename, 'w') as f:
        f.writelines(main_file)

    test_file = """from aoc2020.day{} import part_a, part_b


def test_{}a():
    # assert(part_a('data/day{}_test1.txt') == 0)
    pass


def test_{}b():
    # assert(part_b('data/day{}_test1.txt') == 0)
    pass
""".format(n, n, n, n, n)

    test_filename = "../../tests/func/test_day{}.py".format(n)
    with open(test_filename, 'w') as f:
        f.writelines(test_file)
