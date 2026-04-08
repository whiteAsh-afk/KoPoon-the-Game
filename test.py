import curses
from title import draw_title_screen
from render import render_all
from player import Player
from map import generate_map

player = Player()
game_map = generate_map(20, 20)


def main(stdscr):
    curses.curs_set(0)

    draw_title_screen(stdscr)
    stdscr.refresh()
    stdscr.getch()

    while True:
        stdscr.clear()

        render_all(stdscr, game_map, player)

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            break


curses.wrapper(main)
