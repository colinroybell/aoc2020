import sys

class Tile:
    def __init__(self,id,lines):
        self.id = id
        self.lines = lines
        self.edges = ["" for j in range(0,8)]
        edges = [['.' for i in range(0,10)] for j in range(0,8)]
   
        for p in range(0,10):
            edges[0][p] = lines[0][p]
            edges[1][p] = lines[p][9]
            edges[2][p] = lines[9][9-p]
            edges[3][p] = lines[9-p][0]
            # 4 to 7 are with a horizontal reflection
            edges[4][p] = lines[0][9-p]
            edges[5][p] = lines[p][0]
            edges[6][p] = lines[9][p]
            edges[7][p] = lines[9-p][9]

        for e in range(0,8):
            self.edges[e] = "".join(edges[e])

    def edge(self,dir, state):
        ref = (state//4)*4
        rot  = state%4
        return self.edges[ref + (rot + dir)%4]
        
class Grid:
    def __init__ (self,size,tiles):
        self.item = [[(0,0) for i in range(0,size)] for j in range(0,size)] 
        self.size = size
        self.tiles = tiles
        self.used = [False for i in range(len(tiles))]       
        self.fill = []
        for total in range(0,2*size-1):
            for x in range(0,size):
                y = total - x
                if 0 <= y < size:
                    self.fill.append((x,y))            

    def recurse(self, count):
        if count == self.size * self.size:
            # Done
            size = self.size
            return self.tiles[self.item[0][0][0]].id * self.tiles[self.item[0][size-1][0]].id * self.tiles[self.item[size-1][0][0]].id * self.tiles[self.item[size-1][size-1][0]].id
        else:
            loc = self.fill[count]
          
            if loc[0] > 0:
                (above, above_state) = self.item[loc[0]-1][loc[1]]
                target_top_edge = self.tiles[above].edge(2,above_state)[::-1]
            else:
                target_top_edge = ""  

            if loc[1] > 0:
                (left, left_state) = self.item[loc[0]][loc[1]-1]
                target_left_edge = self.tiles[left].edge(1,left_state)[::-1]
            else:
                target_left_edge = ""      
            for n, t in enumerate(self.tiles):
                if self.used[n]:
                    continue
                for state in range(0,8):
                    top_edge = t.edge(0,state)
                    left_edge = t.edge(3,state)    
                    if (top_edge == target_top_edge or target_top_edge == "") and (left_edge == target_left_edge or target_left_edge == ""):
                        self.item[loc[0]][loc[1]] = (n,state)
                        self.used[n] = True
                        r = self.recurse(count + 1)
                        if r > 0:
                            return r
                        else:
                            # backtrack
                            self.item[loc[0]][loc[1]] = (0,0)
                            self.used[n] = False
            return 0







def part_a(filename):
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
                tiles.append(Tile(id,lines))
                tile_count += 1
                lines = []
            count = (count + 1) % 12            
    if tile_count == 9:
        size = 3
    else:
        size = 12

    grid = Grid(size, tiles)
    return grid.recurse(0)


def part_b(filename):
    return 0


def entry():
    if 'a' in sys.argv:
        print(part_a('data/day20.txt'))
    if 'b' in sys.argv:
        print(part_b('data/day20.txt'))


if __name__ == "__main__":
    entry()
