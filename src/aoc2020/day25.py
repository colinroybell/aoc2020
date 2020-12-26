import sys


def loop_size(public_key):
    v = 1
    count = 0
    while v != public_key:
        v = (v*7) % 20201227
        count += 1
    return count


def transform(subject, loop):
    v = 1
    for _ in range(0, loop):
        v = (v*subject) % 20201227
    return v


def part_a(card_pub, door_pub):
    card_loop = loop_size(card_pub)
    door_loop = loop_size(door_pub)

    enc_card = transform(door_pub, card_loop)
    enc_door = transform(card_pub, door_loop)

    assert(enc_card == enc_door)
    return enc_card


def part_b():
    return "Happy Christmas!"


def entry():
    if 'a' in sys.argv:
        print(part_a(16616892, 14505727))
    if 'b' in sys.argv:
        print(part_b())


if __name__ == "__main__":
    entry()
