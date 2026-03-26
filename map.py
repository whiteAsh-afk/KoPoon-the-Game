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


# print the map
def draw_map(map, player):
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if x == player.x and y == player.y:
                print("[P]", end="")
            else:
                print(f"[{tile}]", end="")
        print("")
