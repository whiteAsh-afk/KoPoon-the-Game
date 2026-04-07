# map_generator
def generate_map(row, column):
    map = []
    for x in range(row):
        tiles = []
        for y in range(column):
            if y == 0 or y == row - 1 or x == 0 or x == column - 1:
                tiles.append("#")
            else:
                tiles.append(".")
        map.append(tiles)
    return map
