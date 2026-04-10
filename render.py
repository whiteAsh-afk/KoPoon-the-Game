import curses

MARGIN_X = 2
MARGIN_Y = 2
HUD_HEIGHT = 9


def draw_hud(stdscr):
    height, width = stdscr.getmaxyx()

    # layout bounds
    top = MARGIN_Y
    bottom = height - MARGIN_Y
    left = MARGIN_X
    right = width - MARGIN_X - 1

    # hud position
    hud_top = bottom - HUD_HEIGHT

    # inner
    inner_width = right - left + 1
    inner_height = bottom - top

    # seperators positions
    sep1 = left + inner_width // 2
    sep2 = left + (inner_width // 4) * 3

    # horizontal lines
    stdscr.hline(top - 1, left, curses.ACS_HLINE, inner_width)
    stdscr.hline(hud_top, left, curses.ACS_HLINE, inner_width)
    stdscr.hline(bottom, left, curses.ACS_HLINE, inner_width)

    # vertical lines
    stdscr.vline(top, left, curses.ACS_VLINE, inner_height)
    stdscr.vline(top, right, curses.ACS_VLINE, inner_height)

    # corners
    stdscr.addch(top - 1, left, curses.ACS_ULCORNER)
    stdscr.addch(top - 1, right, curses.ACS_URCORNER)

    stdscr.addch(hud_top, left, curses.ACS_LTEE)
    stdscr.addch(hud_top, right, curses.ACS_RTEE)

    stdscr.addch(bottom, left, curses.ACS_LLCORNER)
    stdscr.addch(bottom, right, curses.ACS_LRCORNER)

    # seperators inside HUD
    stdscr.vline(hud_top, sep1, curses.ACS_VLINE, HUD_HEIGHT)
    stdscr.vline(hud_top, sep2, curses.ACS_VLINE, HUD_HEIGHT)

    stdscr.addch(hud_top, sep1, curses.ACS_TTEE)
    stdscr.addch(hud_top, sep2, curses.ACS_TTEE)

    stdscr.addch(bottom, sep1, curses.ACS_BTEE)
    stdscr.addch(bottom, sep2, curses.ACS_BTEE)


def draw_map(stdscr, game_map, player):
    stdscr.clear()
    for y, row in enumerate(game_map):
        for x, tile in enumerate(row):
            render_x = (x * 3) + MARGIN_X + 1
            render_y = y + MARGIN_Y

            char = "[@]" if (x == player.x and y == player.y) else f"[{tile}]"
            stdscr.addstr(render_y, render_x, char)
    stdscr.refresh()


def render_all(stdscr, game_map, player):
    stdscr.clear()
    draw_hud(stdscr)
    draw_map(stdscr, game_map, player)
    stdscr.refresh()
