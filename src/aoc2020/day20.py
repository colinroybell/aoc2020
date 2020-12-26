import sys


class Tile:
    def __init__(self, id, lines):
        self.id = id
        self.lines = lines
        self.edges = ["" for j in range(0, 8)]
        edges = [['.' for i in range(0, 10)] for j in range(0, 8)]

        for p in range(0, 10):
            edges[0][p] = lines[0][p]
            edges[1][p] = lines[p][9]
            edges[2][p] = lines[9][9-p]
            edges[3][p] = lines[9-p][0]
            # 4 to 7 are with a horizontal reflection
            edges[4][p] = lines[0][9-p]
            edges[5][p] = lines[p][0]
            edges[6][p] = lines[9][p]
            edges[7][p] = lines[9-p][9]

        for e in range(0, 8):
            self.edges[e] = "".join(edges[e])

    def edge(self, dir, state):
        ref = (state//4) * 4
        rot = state % 4
        return self.edges[ref + (rot + dir) % 4]

    # Horrendous. Fix me.
    def inner(self, state):
        grid = [['.' for i in range(0, 8)] for j in range(0, 8)]

        for y in range(0, 8):
            for x in range(0, 8):
                if state == 0:
                    grid[y][x] = self.lines[y+1][x+1]
                if state == 3:
                    grid[y][x] = self.lines[8-x][y+1]
                if state == 2:
                    grid[y][x] = self.lines[8-y][8-x]
                if state == 1:
                    grid[y][x] = self.lines[x+1][8-y]
                if state == 4:
                    grid[y][x] = self.lines[y+1][8-x]
                if state == 7:
                    grid[y][x] = self.lines[8-x][8-y]
                if state == 6:
                    grid[y][x] = self.lines[8-y][x+1]
                if state == 5:
                    grid[y][x] = self.lines[x+1][y+1]

        inner = []
        for y in range(0, 8):
            line = ""
            for x in range(0, 8):
                line += grid[y][x]
            inner.append(line)

        return inner


class Grid:
    def __init__(self, size, tiles):
        self.item = [[(0, 0) for i in range(0, size)] for j in range(0, size)]
        self.size = size
        self.tiles = tiles
        self.used = [False for i in range(len(tiles))]
        self.fill = []
        for total in range(0, 2*size-1):
            for x in range(0, size):
                y = total - x
                if 0 <= y < size:
                    self.fill.append((x, y))

    def recurse(self, count):
        if count == self.size * self.size:
            # Done
            size = self.size

            return self.tiles[self.item[0][0][0]].id * \
                self.tiles[self.item[0][size-1][0]].id * \
                self.tiles[self.item[size-1][0][0]].id * \
                self.tiles[self.item[size-1][size-1][0]].id

        else:
            loc = self.fill[count]

            if loc[0] > 0:
                (above, above_state) = self.item[loc[0]-1][loc[1]]
                target_top_edge = self.tiles[above].edge(2, above_state)[::-1]
            else:
                target_top_edge = ""

            if loc[1] > 0:
                (left, left_state) = self.item[loc[0]][loc[1]-1]
                target_left_edge = self.tiles[left].edge(1, left_state)[::-1]
            else:
                target_left_edge = ""
            for n, t in enumerate(self.tiles):
                if self.used[n]:
                    continue
                for state in range(0, 8):
                    top_edge = t.edge(0, state)
                    left_edge = t.edge(3, state)

                    # This is the alignment pycodestyle insists on...
                    if (top_edge == target_top_edge or
                        target_top_edge == "") and \
                        (left_edge == target_left_edge or
                            target_left_edge == ""):

                        self.item[loc[0]][loc[1]] = (n, state)
                        self.used[n] = True
                        r = self.recurse(count + 1)
                        if r > 0:
                            return r
                        else:
                            # backtrack
                            self.item[loc[0]][loc[1]] = (0, 0)
                            self.used[n] = False
            return 0

    def build_inner(self):
        new_grid = []
        new_start = ["" for i in range(0, 8)]
        for y in range(0, self.size):
            new_rows = new_start.copy()
            for x in range(0, self.size):
                (tile,  state) = self.item[y][x]
                inner = self.tiles[tile].inner(state)
                print(y, x, self.tiles[tile].id, state)
                for r in range(0, 8):
                    print(inner[r])
                    new_rows[r] += inner[r]
            new_grid.extend(new_rows)
        return new_grid


def rot(loc, state):
    (x, y) = loc
    if state == 0:
        return (x, y)
    if state == 1:
        return (y, -x)
    if state == 2:
        return (-x, -y)
    if state == 3:
        return (-y, x)
    if state == 4:
        return (-x, y)
    if state == 5:
        return (-y, -x)
    if state == 6:
        return (x, -y)
    if state == 7:
        return (y, x)


def delta(pos, dir):
    return (pos[0]+dir[0], pos[1]+dir[1])


def count_monsters(source_grid, monster, state):
    size = len(source_grid)
    # 0 for ., 1 for #, 2 for monster
    grid = [[0 for i in range(0,  size)] for j in range(0, size)]
    monsters = 0

    for j in range(0, size):
        for i in range(0, size):
            if source_grid[j][i] == '#':
                grid[j][i] = 1

    for j in range(0, size):
        for i in range(0, size):
            found = True
            for y in range(0, len(monster)):
                for x in range(0, len(monster[0])):
                    if monster[y][x] == '#':
                        (my, mx) = delta((j, i), rot((y, x), state))
                        if my < 0 or my >= size or mx < 0 or mx >= size or \
                                grid[my][mx] == 0:
                            found = False
            if found:
                print('Found at', j, i)
                monsters += 1
                for y in range(0, len(monster)):
                    for x in range(0, len(monster[0])):
                        if monster[y][x] == '#':
                            (my, mx) = delta((j, i), rot((y, x), state))
                            grid[my][mx] = 2

    roughness = 0
    for j in range(0, size):
        for i in range(0, size):
            if grid[j][i] == 1:
                roughness += 1

    return (monsters, roughness)


def both_parts(filename, part):
    lines = []
    tiles = []
    id = 0
    tile_count = 0
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            if count == 0:
                id = int(line[5:9])
            elif count < 11:
                lines.append(line)
            else:
                tiles.append(Tile(id, lines))
                tile_count += 1
                lines = []
            count = (count + 1) % 12
    if tile_count == 9:
        size = 3
    else:
        size = 12

    grid = Grid(size, tiles)
    val = grid.recurse(0)
    if part == 'a':
        return val

    new_grid = grid.build_inner()
    for r in new_grid:
        print(r)

    monster = ["                  # ",
               "#    ##    ##    ###",
               " #  #  #  #  #  #   "]

    r = 0

    for state in range(0, 8):
        (monsters, roughness) = count_monsters(new_grid, monster, state)
        print(state, monsters, roughness)
        if monsters > 0:
            r = roughness
    return r


def part_a(filename):
    return both_parts(filename, 'a')


def part_b(filename):
    return both_parts(filename, 'b')


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day20.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day20.txt'))


if __name__ == "__main__":
    entry()
