import random
import curses

from enemy import random_enemy
from player import Player
from map import generate_map
from battle import battle
from render import draw_map
from title import draw_title_screen
from control import explore_input

player = Player()
game_map = generate_map(30, 30)


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    draw_title_screen(stdscr)
    # stdscr.getch()

    while True:
        draw_map(stdscr, game_map, player)
        key = stdscr.getch()

        if key == ord("q"):
            break
        # render_all(stdscr, game_map, player)
        stdscr.clear()

        moved = False

        moved = explore_input(key, player, game_map)

        if moved:
            if random.random() < 0.05:
                enemy = random_enemy()

                result = battle(stdscr, player, enemy)
                if result == "win":
                    stdscr.clear()
                    stdscr.addstr(10, 2, f"{enemy.name} defeated!")
                    stdscr.refresh()
                    stdscr.getch()
                elif result == "lose":
                    stdscr.clear()
                    stdscr.addstr(10, 2, "KoPoon was defeated...")
                    stdscr.refresh()
                    stdscr.getch()
                elif result == "run":
                    stdscr.clear()
                    stdscr.addstr(10, 2, "You escaped!")
                    stdscr.refresh()
                    stdscr.getch()
                elif result == "quit":
                    break


curses.wrapper(main)
