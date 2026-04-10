import curses


def explore_input(key, player, game_map):
    if key == curses.KEY_UP:
        return player.move(0, -1, game_map)
    elif key == curses.KEY_DOWN:
        return player.move(0, 1, game_map)
    elif key == curses.KEY_LEFT:
        return player.move(-1, 0, game_map)
    elif key == curses.KEY_RIGHT:
        return player.move(1, 0, game_map)
