import sys


def is_sum_of(n, array):
    size = len(array)
    for i in range(0, size):
        for j in range(i+1, size):
            if n == array[i] + array[j]:
                return 1
    return 0


def part_a(filename, count):
    array = []
    with open(filename, 'r') as f:
        for line in f:
            array.append(int(line))
    for i in range(count, len(array)):
        if not is_sum_of(array[i], array[i-count:i]):
            return array[i]
    return 0


def part_b(filename, count):
    array = []
    with open(filename, 'r') as f:
        for line in f:
            array.append(int(line))
    total = part_a(filename, count)
    start = 0
    finish = 0
    sum_ = 0
    while sum_ != total:
        if sum_ <= total:
            sum_ += array[finish]
            finish += 1
            assert(finish <= len(array))
        else:
            sum_ -= array[start]
            start += 1
    return min(array[start:finish]) + max(array[start:finish])


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day09.txt', 25))
    if 'b' in sys.argv:
        print(part_b('data/day09.txt', 25))


if __name__ == "__main__":
    entry()
