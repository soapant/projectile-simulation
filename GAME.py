import time
import pygame
import sys
import math
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Game")

background = pygame.image.load("SPRITES\\background.png").convert()
background = pygame.transform.scale(background, (1080, 720))

Bow = pygame.image.load("SPRITES\\Bow.png").convert_alpha()
scaled_bow = pygame.transform.scale(Bow, (149, 335))

arrow = pygame.image.load("SPRITES\\arrow.png").convert_alpha()
scaled_arrow = pygame.transform.scale(arrow, (306, 51))
# variables galore
bow_x = 100
bow_y = 350
arrow_x = 100
arrow_y = 350
vibe_x = 0
vibe_y = 0
angle = 0
angle2 = 0
right_hold_start = None
right_action_done = False
arrow_flying = False
arrow_pos_x = arrow_x
arrow_pos_y = arrow_y
arrow_vx = 0
arrow_vy = 0
arrow_target = (0, 0)
gravity = 0.1
arrow_timer = 0
arrow_max_time = 5.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()

    mouse_buttons = pygame.mouse.get_pressed()
    if not mouse_buttons[2] and not arrow_flying:
        dx, dy = mouse_x - bow_x, mouse_y - bow_y
        dn, di = mouse_x - arrow_x, mouse_y - arrow_y
        angle = math.degrees(math.atan2(-dy, dx))
        angle2 = math.degrees(math.atan2(-di, dn))

    current_time = time.time()

    if mouse_buttons[2]:
        vibe_x = random.randint(-1, 1)
        vibe_y = random.randint(-1, 1)
        if right_hold_start is None:
            right_hold_start = current_time

    else:
        if right_hold_start is not None:
            held_time = current_time - right_hold_start
            if held_time >= 1.0 and not arrow_flying:
                arrow_target = pygame.mouse.get_pos()
                arrow_flying = True
                arrow_pos_x = arrow_x
                arrow_pos_y = arrow_y
                arrow_timer = arrow_max_time

                dx = arrow_target[0] - arrow_x
                dy = arrow_target[1] - arrow_y
                distance = math.hypot(dx, dy)

                speed = 15
                arrow_vx = (dx / distance) * speed
                arrow_vy = (dy / distance) * speed

                print(arrow_target)

            right_hold_start = None

        if arrow_flying:
            arrow_timer -= 1 / 60
            #ooooh gravity
            arrow_vy += gravity

            arrow_pos_x += arrow_vx
            arrow_pos_y += arrow_vy

            angle2 = math.degrees(math.atan2(-arrow_vy, arrow_vx))
            #resets the arrow if it is below the screen or timer ran out
            if arrow_timer <= 0 or arrow_pos_y > 720 or arrow_pos_x > 1080 or arrow_pos_x < 0:
                arrow_flying = False
                arrow_pos_x = arrow_x
                arrow_pos_y = arrow_y
                arrow_vx = 0
                arrow_vy = 0

    rotated_bow = pygame.transform.rotate(scaled_bow, angle)

    rotated_arrow = pygame.transform.rotate(scaled_arrow, angle2)

    bow_rect = rotated_bow.get_rect(center=(bow_x, bow_y))

    arrow_rect = rotated_arrow.get_rect(center=(arrow_pos_x + vibe_x, arrow_pos_y + vibe_y))

    screen.blit(background, (0, 0))

    screen.blit(rotated_bow, bow_rect)

    screen.blit(rotated_arrow, (arrow_rect.x + vibe_x, arrow_rect.y + vibe_y))

    pygame.display.flip()

    clock.tick(60)