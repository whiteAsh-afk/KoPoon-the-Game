import random
import curses
from helpers import menu_box, message_box


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.state = "menu"
        self.message = ""

    # def attack(self)


def battle(stdscr, player, enemy):
    curses.curs_set(0)
    stdscr.keypad(True)

    options = ["Attack", "Run"]
    selected = 0
    while True:
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
        # for i, option in enumerate(menu):
        #     if i == selected:
        #         stdscr.addstr(7 + i, 4, f"> {option}")
        #     else:
        #         stdscr.addstr(7 + i, 4, f"  {option}")

        # stdscr.refresh()
        #
        # key = stdscr.getch()
        # if key == ord("q") or key == ord("Q"):
        #     return "quit"
        # elif key == curses.KEY_UP:
        #     selected = (selected - 1) % len(menu)
        # elif key == curses.KEY_DOWN:
        #     selected = (selected + 1) % len(menu)
        # # return/ enter
        # elif key == 10:
        # choose Attack
        if choice == "Attack":
            damage = player.attack
            enemy.take_damage(damage)

            message_box(
                stdscr,
                10,
                2,
                3,
                70,
                [f"KoPoon hit the {enemy.name} for {damage} damage!"],
            )

            # enemy defeated
            if not enemy.is_alive():
                stdscr.addstr(12, 2, f"{enemy.name} defeated!")
                stdscr.refresh()
                stdscr.getch()
                break

            # enemy attack
            damage = enemy.attack
            player.take_damage(damage)

            stdscr.addstr(11, 2, f"{enemy.name} hit KoPoon for {damage} damage!")
            stdscr.refresh()
            stdscr.getch()

        # choose run
        elif choice == "Run":
            if random.random() < 0.5:
                return "run"

            else:
                stdscr.addstr(10, 2, "Couldn't escape!")
                stdscr.refresh()
                stdscr.getch()

                damage = enemy.attack
                player.take_damage(damage)

                stdscr.addstr(11, 2, f"{enemy.name} hits you for {damage} damage!")
                stdscr.refresh()
                stdscr.getch()


# def battle(player, enemy):
