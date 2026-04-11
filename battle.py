import random
import curses
from helpers import menu_box, message_box


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.state = "menu"
        self.message = ""

    def player_attack(self):
        damage = self.player.power
        self.enemy.take_damage(damage)

        self.message = f"KoPoon hit the {self.enemy.name} for {damage} damage!"

        if not self.enemy.is_alive():
            self.state = "win"
            return
        self.enemy_attack()

    def enemy_attack(self):
        damage = self.enemy.power
        self.player.take_damage(damage)

        self.message += f"\n{self.enemy.name} hit KoPoon for {damage} damage!"

        if not self.player.is_alive():
            self.state = "lose"

    def run(self):
        if random.random() < 0.5:
            self.state = "run"
        else:
            self.message = "Could'nt escape"
            self.enemy_attack()


def battle(stdscr, player, enemy):
    battle = Battle(player, enemy)

    curses.curs_set(0)
    stdscr.keypad(True)

    options = ["Attack", "Run"]
    selected = 0

    while True:
        if battle.state in ["win", "lose", "run"]:
            return battle.state

        if not player.is_alive():
            return "lose"

        if not enemy.is_alive():
            return "win"

        stdscr.clear()

        # battle info
        message_box(
            stdscr,
            1,
            2,
            9,
            30,
            [
                f"You encountered {enemy.name}!",
                f"KoPoon HP: {player.hp}",
                f"Enemy Hp: {enemy.hp}",
            ],
        )
        # stdscr.addstr(1, 2, f"You encountered {enemy.name}!")
        # stdscr.addstr(3, 2, f"KoPoon HP: {player.hp}")
        # stdscr.addstr(4, 2, f"Enemy Hp: {enemy.hp}")

        # draw menu
        selected = menu_box(stdscr, 10, 10, 40, options, selected)
        choice = options[selected]

        # choose Attack
        if choice == "Attack":
            battle.player_attack()

        # choose run
        elif choice == "Run":
            battle.run()

        if battle.message:
            message_box(stdscr, 10, 2, 5, 60, battle.message.split("\n"))
