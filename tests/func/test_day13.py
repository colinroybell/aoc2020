from aoc2020.day13 import part_a, part_b


def test_13a():
    assert(part_a('data/day13_test1.txt') == 295)


def test_13b():
    assert(part_b('data/day13_test1.txt') == 1068781)
    assert(part_b('data/day13_test2.txt') == 3417)
