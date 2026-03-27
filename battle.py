from helpers import draw_text, clear, wait
import random


def battle(player, enemy):
    print(f"A wild {enemy.name} appear!!")

    while player.is_alive() and enemy.is_alive():
        clear()
        print("=====BATTLE=====")

        print(f"KoPoon HP: {player.hp}")
        print(f"enemy: {enemy.name}")
        print(f"enemy HP: {enemy.hp}")
        print("What will KoPoon do?")
        print("1. Attack")
        print("2. Run")

        choice = input("> ")

        if choice == "1":
            damage = player.attack
            enemy.take_damage(damage)

            print(f"KoPoon hit the {enemy.name} for {damage} damage!")
            wait()

            if not enemy.is_alive():
                print(f"{enemy.name} defeated!")
                wait()
                break

            damage = enemy.attack
            player.take_damage(damage)

            print(f"{enemy.name} hit KoPoon for {damage} damage!")
            wait()
        elif choice == "2":
            if random.random() < 0.5:
                print("You escaped!")
                wait()
                break
            else:
                print("Couldn't escape!")
                wait()

                damage = enemy.attack
                player.take_damage(damage)

                print(f"{enemy.name} hits you for {damage} damage!")
                wait()
        else:
            print("Invalid input.")
            wait()
    print("\nBattle ended\n")
    wait()
