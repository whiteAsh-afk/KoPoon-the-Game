# map_generator
def generate_map(row, column):
    map = []
    for i in range(row):
        tiles = []
        for i in range(column):
            tiles.append(".")
        map.append(tiles)
    return map


# print the map
def draw_map(map):
    for row in map:
        for tiles in row:
            print(f"[{tiles}]", end="")
        print()
