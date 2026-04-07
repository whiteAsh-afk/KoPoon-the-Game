import random
import curses

from enemy import random_enemy
from player import Player
from map import generate_map
from battle import battle
from hud import draw_hud

player = Player()
game_map = generate_map(10, 10)


def draw_map(stdscr, game_map, player):
    stdscr.clear()

    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            if x == player.x and y == player.y:
                stdscr.addstr(y, x * 3, "[P]")
            else:
                stdscr.addstr(y, x * 3, f"[{tile}]")

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)

    while player.is_alive():
        draw_hud(stdscr)
        draw_map(stdscr, game_map, player)

        key = stdscr.getch()

        if key == ord("q"):
            break

        elif key == curses.KEY_UP:
            player.move(0, -1, game_map)
        elif key == curses.KEY_DOWN:
            player.move(0, 1, game_map)
        elif key == curses.KEY_LEFT:
            player.move(-1, 0, game_map)
        elif key == curses.KEY_RIGHT:
            player.move(1, 0, game_map)

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
