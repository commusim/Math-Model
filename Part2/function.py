def pos_xor(x, y, maps):
    add = 0
    for _ in range(9):
        add += maps[_][x][y]
    return add


def col_xor(num, y, maps):
    add = 0
    for _ in range(9):
        add += maps[num][_][y]
    return add


def row_xor(x, num, maps):
    add = 0
    for _ in range(9):
        add += maps[num][x][_]
    return add

def ku_xor(x,y,maps):
    add = 0
    return add

def init(num_map, maps):
    for x in range(9):
        for y in range(9):
            num = num_map[x][y]
            if num != 0:
                maps[num - 1][x][y] = 1
