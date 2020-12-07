from aoc2020.day07 import part_a, part_b


def test_07a():
    assert(part_a('data/day07_test1.txt') == 4)


def test_07b():
    assert(part_b('data/day07_test1.txt') == 32)
    assert(part_b('data/day07_test2.txt') == 126)
