import math
import pygame
from pygame import KEYDOWN

pygame.init()

res = (640, 480)
bg_color = (0, 0, 0)
test_color = (255, 0, 255)
screen = pygame.display.set_mode([res[0], res[1]])

running = True
thing = 0

size = 50
rect_init = (res[0] / 2 - size / 2, res[1] / 2 - size / 2, size, size)
rect_pos_x = rect_init[0]
rect_pos_y = rect_init[1]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        player_movement = pygame.key.get_pressed()
        if player_movement[pygame.K_d]:
            rect_pos_x += 1
        if player_movement[pygame.K_a]:
            rect_pos_x -= 1
        if player_movement[pygame.K_w]:
            rect_pos_y -= 1
        if player_movement[pygame.K_s]:
            rect_pos_y += 1

    screen.fill(bg_color)
    pygame.draw.rect(screen, test_color, (rect_pos_x, rect_pos_y, size, size))

    pygame.display.flip()
pygame.quit()