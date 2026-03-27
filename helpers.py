import os
import time
import pygame


# clear the battle screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")


def wait():
    time.sleep(2)


def draw_text(screen, text, x, y):
    font = pygame.font.SysFont("monospace", 24)
    text_surface = font.render(text, True, (255, 255, 255))
    screen.blit(text_surface, (x, y))
