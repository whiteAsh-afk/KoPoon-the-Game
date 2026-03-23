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


# player's action
def player_turn():
    action = input("What will KoPoon do?\n"
                   "1. Attack\n"
                   "2. Heal\n"
                   "3. Wait")
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
while not is_dead(player):
    battle_screen()
    player_turn()
    enemy_turn()
    if is_dead(enemy):
        print("The enemy is defeated!")
        break
