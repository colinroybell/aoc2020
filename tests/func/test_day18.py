from aoc2020.day18 import part_a, part_b


def test_18a():
    assert(part_a('data/day18_test1.txt') == 71)
    assert(part_a('data/day18_test2.txt') == 51)
    assert(part_a('data/day18_test3.txt') == 26)
    assert(part_a('data/day18_test4.txt') == 437)
    assert(part_a('data/day18_test5.txt') == 12240)
    assert(part_a('data/day18_test6.txt') == 13632)


def test_18b():
    assert(part_b('data/day18_test1.txt') == 231)
    assert(part_b('data/day18_test2.txt') == 51)
    assert(part_b('data/day18_test3.txt') == 46)
    assert(part_b('data/day18_test4.txt') == 1445)
    assert(part_b('data/day18_test5.txt') == 669060)
    assert(part_b('data/day18_test6.txt') == 23340)
