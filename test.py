from player import Player
from map import generate_map, draw_map

player = Player()

map = generate_map(10, 10)

while True:
    draw_map(map, player)

    move = input("Move (WASD): ")
    move = move.lower()
    if move == "w":
        player.move(0, -1, map)
    elif move == "s":
        player.move(0, 1, map)
    elif move == "a":
        player.move(-1, 0, map)
    elif move == "d":
        player.move(1, 0, map)
    else:
        print("Invalid input")
        continue
