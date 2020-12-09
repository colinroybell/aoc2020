from aoc2020.day09 import part_a, part_b


def test_09a():
    assert(part_a('data/day09_test1.txt', 5) == 127)


def test_09b():
    assert(part_b('data/day09_test1.txt', 5) == 62)
