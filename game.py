import os
import time

# define player stats
player = {
        "hp" : 100,
        "dmg" : 20
        }

# define enemy stats
enemy = {
        "hp" : 70,
        "dmg" : 15
        }

# print the battle screen
def battle_screen():
    print(f"KoPoon HP: {player['hp']}")
    print(f"enemy HP: {enemy['hp']}")

# clear the battle screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# player's action
def player_turn():
    action = input("What will KoPoon do?\n"
                   "1. Attack\n"
                   "2. Heal\n"
                   "3. Wait\n")
    if action == "1":
        enemy["hp"] -= player["dmg"]
        print(f"KoPoon attack the enemy!\nDamage: {player['dmg']}")
    elif action == "2":
        player["hp"] += 10
        print("KoPoon heal a bit.")
    elif action == "3":
        print("KoPoon wait and do no action.")
        
# enemy's action
def enemy_turn():
    player["hp"] -= enemy["dmg"]
    print(f"The enemy attack!\nDamage: {enemy['dmg']}")

# enemy hp checker
def is_dead(character):
    return character["hp"] <= 0

#init the gameplay
game_running = True
while game_running:
    clear()
    battle_screen()
    player_turn()
    time.sleep(2)
    if is_dead(enemy):
        print("The enemy is defeated!")
        game_running = False
    enemy_turn()
    time.sleep(2)
    if is_dead(player):
        print("KoPoon is dead!")
        game_running = False
