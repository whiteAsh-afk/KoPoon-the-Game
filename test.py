import pygame
import sys
from map import draw_map, generate_map
from player import Player

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map test")

player = Player()
game_map = generate_map(10, 10)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move(0, -1, game_map)
            elif event.key == pygame.K_s:
                player.move(0, 1, game_map)
            elif event.key == pygame.K_a:
                player.move(-1, 0, game_map)
            elif event.key == pygame.K_d:
                player.move(1, 0, game_map)

    screen.fill((0, 0, 0))

    draw_map(game_map, player, screen)

    pygame.display.flip()
