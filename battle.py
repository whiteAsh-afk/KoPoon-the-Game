import random
import curses


def battle(stdscr, player, enemy):
    curses.curs_set(0)
    stdscr.keypad(True)

    menu = ["Attack", "Run"]
    selected = 0

    while True:
        if not player.is_alive():
            stdscr.addstr(5, 5, "KoPoon was defeated...")
            stdscr.refresh()
            stdscr.getch()
            break

        if not enemy.is_alive():
            stdscr.addstr(5, 5, f"{enemy.name} defeated")
            stdscr.refresh()
            stdscr.getch()
            break

        stdscr.clear()

        # battle info
        stdscr.addstr(1, 2, f"You encountered {enemy.name}!")
        stdscr.addstr(3, 2, f"KoPoon HP: {player.hp}")
        stdscr.addstr(4, 2, f"Enemy Hp: {enemy.hp}")

        # draw menu
        for i, option in enumerate(menu):
            if i == selected:
                stdscr.addstr(7 + i, 4, f"> {option}")
            else:
                stdscr.addstr(7 + i, 4, f"  {option}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected = (selected - 1) % len(menu)
        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(menu)
        # return/ enter
        elif key == 10:
            # choose Attack
            if selected == 0:
                damage = player.attack
                enemy.take_damage(damage)

                stdscr.addstr(
                    10, 2, f"KoPoon hit the {enemy.name} for {damage} damage!"
                )
                stdscr.refresh()
                stdscr.getch()

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
            elif selected == 1:
                if random.random() < 0.5:
                    stdscr.addstr(10, 2, "You escaped!")
                    stdscr.refresh()
                    stdscr.getch()
                    break
                else:
                    stdscr.addstr(10, 2, "Couldn't escape!")
                    stdscr.refresh()
                    stdscr.getch()

                    damage = enemy.attack
                    player.take_damage(damage)

                    stdscr.addstr(11, 2, f"{enemy.name} hits you for {damage} damage!")
                    stdscr.refresh()
                    stdscr.getch()
