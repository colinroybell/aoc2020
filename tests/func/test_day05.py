from aoc2020.day05 import part_a, seat_id, part_b


def test_05a():
    assert(seat_id("FBFBBFFRLR") == 357)
    assert(seat_id("BFFFBBFRRR") == 567)
    assert(seat_id("FFFBBBFRRR") == 119)
    assert(seat_id("BBFFBBFRLL") == 820)


def test_05b():
    # assert(part_b('data/day05_test1.txt') == 0)
    pass
