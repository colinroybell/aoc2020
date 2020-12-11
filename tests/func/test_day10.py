from aoc2020.day10 import part_a, part_b


def test_10a():
    assert(part_a('data/day10_test1.txt') == 35)
    assert(part_a('data/day10_test2.txt') == 220)


def test_10b():
    assert(part_b('data/day10_test1.txt') == 8)
    assert(part_b('data/day10_test2.txt') == 19208)
