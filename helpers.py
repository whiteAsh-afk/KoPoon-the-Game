import curses


def draw_box(stdscr, y, x, box_height, box_width):
    # draw borders
    stdscr.hline(y, x, curses.ACS_HLINE, box_width)
    stdscr.hline(y + box_height, x, curses.ACS_HLINE, box_width)
    stdscr.vline(y, x, curses.ACS_VLINE, box_height)
    stdscr.vline(y, x + box_width, curses.ACS_VLINE, box_height)

    stdscr.addch(y, x, curses.ACS_ULCORNER)
    stdscr.addch(y, x + box_width, curses.ACS_URCORNER)
    stdscr.addch(y + box_height, x, curses.ACS_LLCORNER)
    stdscr.addch(y + box_height, x + box_width, curses.ACS_LRCORNER)
