from wcwidth import wcswidth
from helpers import menu_box

# TITLE = [
#     "   ▄█   ▄█▄  ▄██████▄     ▄██████▄   ▄██████▄   ▄██████▄  ███▄▄▄▄   ",
#     "  ███ ▄███▀ ███    ███   ███    ███ ███    ███ ███    ███ ███▀▀▀██▄ ",
#     "  ███▐██▀   ███    ███   ███    ███ ███    ███ ███    ███ ███   ███ ",
#     " ▄█████▀    ███    ███   ███    ███ ███    ███ ███    ███ ███   ███ ",
#     "▀▀█████▄    ███    ███ ▀█████████▀  ███    ███ ███    ███ ███   ███ ",
#     "  ███▐██▄   ███    ███   ███        ███    ███ ███    ███ ███   ███ ",
#     "  ███ ▀███▄ ███    ███   ███        ███    ███ ███    ███ ███   ███ ",
#     "  ███   ▀█▀  ▀██████▀   ▄████▀       ▀██████▀   ▀██████▀   ▀█   █▀  ",
#     "  ▀                                                                 ",
# ]

# TITLE = [
#     "      :::    :::       ::::::::       :::::::::       ::::::::       ::::::::       ::::    ::: ",
#     "     :+:   :+:       :+:    :+:      :+:    :+:     :+:    :+:     :+:    :+:      :+:+:   :+:  ",
#     "    +:+  +:+        +:+    +:+      +:+    +:+     +:+    +:+     +:+    +:+      :+:+:+  +:+   ",
#     "   +#++:++         +#+    +:+      +#++:++#+      +#+    +:+     +#+    +:+      +#+ +:+ +#+    ",
#     "  +#+  +#+        +#+    +#+      +#+            +#+    +#+     +#+    +#+      +#+  +#+#+#     ",
#     " #+#   #+#       #+#    #+#      #+#            #+#    #+#     #+#    #+#      #+#   #+#+#      ",
#     "###    ###       ########       ###             ########       ########       ###    ####       ",
# ]

TITLE = [
    "   .S    S.     sSSs_sSSs     .S_sSSs      sSSs_sSSs      sSSs_sSSs     .S_sSSs    ",
    "  .SS    SS.   d%%SP~YS%%b   .SS~YS%%b    d%%SP~YS%%b    d%%SP~YS%%b   .SS~YS%%b   ",
    "  S%S    S&S  d%S'     `S%b  S%S   `S%b  d%S'     `S%b  d%S'     `S%b  S%S   `S%b  ",
    "  S%S    d*S  S%S       S%S  S%S    S%S  S%S       S%S  S%S       S%S  S%S    S%S  ",
    "  S&S   .S*S  S&S       S&S  S%S    d*S  S&S       S&S  S&S       S&S  S%S    S&S  ",
    "  S&S_sdSS'   S&S       S&S  S&S   .S*S  S&S       S&S  S&S       S&S  S&S    S&S  ",
    "  S&S~YSSY%b  S&S       S&S  S&S_sdSSS   S&S       S&S  S&S       S&S  S&S    S&S  ",
    "  S&S    `S%  S&S       S&S  S&S~YSSY    S&S       S&S  S&S       S&S  S&S    S&S  ",
    "  S*S     S%  S*b       d*S  S*S         S*b       d*S  S*b       d*S  S*S    S*S  ",
    "  S*S     S&  S*S.     .S*S  S*S         S*S.     .S*S  S*S.     .S*S  S*S    S*S  ",
    "  S*S     S&   SSSbs_sdSSS   S*S          SSSbs_sdSSS    SSSbs_sdSSS   S*S    S*S  ",
    "  S*S     SS    YSSP~YSSY    S*S           YSSP~YSSY      YSSP~YSSY    S*S    SSS  ",
    "  SP                         SP                                        SP          ",
    "  Y                          Y                                         Y           ",
]


def draw_title(stdscr, title):
    h, w = stdscr.getmaxyx()
    y = (h // 2) - (len(title) // 2)

    for i, line in enumerate(title):
        x = (w // 2) - (wcswidth(line) // 2)
        stdscr.addstr(y + i, x, "|" + line + "|")


# def center_text(stdscr, y, x, width, text, highlight=False):
#     padded_text = f" {text} "
#     text_x = x + (width // 2) - (len(padded_text) // 2)
#     if highlight:
#         stdscr.attron(curses.A_REVERSE)
#         stdscr.addstr(y, text_x, padded_text)
#         stdscr.attroff(curses.A_REVERSE)
#     else:
#         stdscr.addstr(y, text_x, padded_text)


def draw_title_screen(stdscr):
    height, width = stdscr.getmaxyx()

    draw_title(stdscr, TITLE)

    box_width = 40

    box_top = (height // 3) * 2
    box_left = width // 2 - box_width // 2

    menu_box(stdscr, box_top, box_left, box_width, ["option1", "option2", "option3"])
