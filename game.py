import random
from enemy import random_enemy
from battle import battle
from player import Player
from map import generate_map, draw_map

player = Player()

game_map = generate_map(10, 10)

while True:
    draw_map(game_map, player)

    key = input("Move (WASD): ")

    if key == "w":
        player.move(0, -1, game_map)
    elif key == "s":
        player.move(0, 1, game_map)
    elif key == "a":
        player.move(-1, 0, game_map)
    elif key == "d":
        player.move(1, 0, game_map)
    else:
        print("Invalid input")

    if random.random() < 0.2:
        enemy = random_enemy()
        battle(player, enemy)
