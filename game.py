import os
import time
from map import generate_map, draw_map
from enemy import random_enemy

# define player stats
player = {"hp": 100, "dmg": 20}


# print the battle screen
def battle_screen():
    os.system("cls" if os.name == "nt" else "clear")
    draw_map(generate_map(5, 5))
    print(f"KoPoon HP: {player['hp']}")
    print(f"enemy: {enemy.name}")
    print(f"enemy HP: {enemy.hp}")
    print("What will KoPoon do?")
    print("1. Attack")
    print("2. Heal")
    print("3. Wait")


# clear the battle screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# player's action
def player_turn():
    while True:
        action = input("> ")
        if action == "1":
            enemy.hp -= player["dmg"]
            print(f"KoPoon attack the enemy!\nDamage: {player['dmg']}")
            break
        elif action == "2":
            player["hp"] += 10
            print("KoPoon heal a bit.")
            break
        elif action == "3":
            print("KoPoon wait and do no action.")
            break
        else:
            print("Invalid input")
            time.sleep(2)
            battle_screen()


# enemy's action
def enemy_turn():
    player["hp"] -= enemy.power
    print(f"The enemy attack!\nDamage: {enemy.power}")


# enemy hp checker
def is_dead(character):
    return character["hp"] <= 0


# init the gameplay
game_running = True
enemy = random_enemy()
while game_running:
    battle_screen()
    player_turn()
    time.sleep(2)
    if enemy.hp <= 0:
        print(f"{enemy.name} is defeated!")
        time.sleep(2)
        enemy = random_enemy()
        enemy.reset()
        continue
    enemy_turn()
    time.sleep(2)
    if is_dead(player):
        print("KoPoon is dead!")
        game_running = False
        break
