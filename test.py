import curses
from hud import draw_hud


def main(stdscr):
    curses.curs_set(0)

    while True:
        stdscr.clear()

        draw_hud(stdscr)

        stdscr.refresh()

        key = stdscr.getch()
        if key == ord("q"):
            break


curses.wrapper(main)
