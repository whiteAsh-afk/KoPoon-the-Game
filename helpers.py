import curses


def _draw_box(stdscr, y, x, h, w):
    # draw borders
    stdscr.hline(y, x, curses.ACS_HLINE, w)
    stdscr.hline(y + h, x, curses.ACS_HLINE, w)
    stdscr.vline(y, x, curses.ACS_VLINE, h)
    stdscr.vline(y, x + w, curses.ACS_VLINE, h)

    stdscr.addch(y, x, curses.ACS_ULCORNER)
    stdscr.addch(y, x + w, curses.ACS_URCORNER)
    stdscr.addch(y + h, x, curses.ACS_LLCORNER)
    stdscr.addch(y + h, x + w, curses.ACS_LRCORNER)

    return y, x, h, w


def message_box(stdscr, y, x, h, w, lines):
    box_y, box_x, box_height, box_width = _draw_box(stdscr, y, x, h, w)
    start_y = box_y + 1 + box_height // 2 - len(lines) // 2

    for i, line in enumerate(lines):
        text_y = start_y + i
        text_x = box_x + box_width // 2 - len(line) // 2
        stdscr.addstr(text_y, text_x, line)


def print_text(stdscr, y, x, width, text, highlight=False):
    text_x = x + (width // 2) - (len(text) // 2)
    if highlight:
        padded_text = f" {text} "
        stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(y, text_x, padded_text)
        stdscr.attroff(curses.A_REVERSE)
    else:
        stdscr.addstr(y, text_x, text)


def menu_box(stdscr, y, x, w, options):
    selected = 0
    h = (len(options) * 2) + 2

    box_y, box_x, box_h, box_w = _draw_box(stdscr, y, x, h, w)

    while True:
        for i, option in enumerate(options):
            text_y = box_y + 2 + (i * 2)
            text_x = box_x + box_w // 2 - len(option) // 2

            if i == selected:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(text_y, text_x, option)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(text_y, text_x, option)

        stdscr.refresh()
        key = stdscr.getch()

        # Navigation
        if key == curses.KEY_UP:
            selected = (selected - 1) % len(options)

        elif key == curses.KEY_DOWN:
            selected = (selected + 1) % len(options)

        elif key == ord("\n"):
            return selected
