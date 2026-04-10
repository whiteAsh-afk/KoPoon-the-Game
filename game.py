import random
import curses

from enemy import random_enemy
from player import Player
from map import generate_map
from battle import battle
from render import draw_map
from title import draw_title_screen

player = Player()
game_map = generate_map(30, 30)


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    draw_title_screen(stdscr)
    stdscr.getch()

    while player.is_alive():
        # render_all(stdscr, game_map, player)
        stdscr.clear()
        draw_map(stdscr, game_map, player)

        key = stdscr.getch()

        moved = False

        if key == ord("q"):
            break

        elif key == curses.KEY_UP:
            moved = player.move(0, -1, game_map)
        elif key == curses.KEY_DOWN:
            moved = player.move(0, 1, game_map)
        elif key == curses.KEY_LEFT:
            moved = player.move(-1, 0, game_map)
        elif key == curses.KEY_RIGHT:
            moved = player.move(1, 0, game_map)

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
