import pygame
import sys
import math
import random
pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Game")

background = pygame.image.load("SPRITES\\background.png").convert()
background = pygame.transform.scale(background, (1080, 720))

Bow = pygame.image.load("SPRITES\\Bow.png").convert_alpha()
scaled_bow = pygame.transform.scale(Bow, (149, 335))

arrow = pygame.image.load("SPRITES\\arrow.png").convert_alpha()
scaled_arrow = pygame.transform.scale(arrow, (306, 51))

bow_x = 100
bow_y = 350
arrow_x = 100
arrow_y = 350
vibe_x = 0
vibe_y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    mouse_x, mouse_y = pygame.mouse.get_pos()


    mouse_buttons = pygame.mouse.get_pressed()
    if not mouse_buttons[2]:
        dx, dy = mouse_x - bow_x, mouse_y - bow_y
        dn, di = mouse_x - arrow_x, mouse_y - arrow_y
        angle = math.degrees(math.atan2(-dy, dx))
        angle2 = math.degrees(math.atan2(-di, dn))
    #fucking hilarious
    if mouse_buttons[2]:
        vibe_x = random.randint(-1, 1)
        vibe_y = random.randint(-1, 1)

    rotated_bow = pygame.transform.rotate(scaled_bow, angle)
    rotated_arrow = pygame.transform.rotate(scaled_arrow, angle2)
    bow_rect = rotated_bow.get_rect(center=(bow_x, bow_y))
    arrow_rect = rotated_arrow.get_rect(center=(arrow_x, arrow_y))
    #draws the background
    screen.blit(background, (0, 0))
    #draws the bow
    screen.blit(rotated_bow, bow_rect)
    #draws the arrow with the vibrating mechanic
    screen.blit(rotated_arrow,(arrow_rect.x + vibe_x, arrow_rect.y + vibe_y))

    pygame.display.flip()

