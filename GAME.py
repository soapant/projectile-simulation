import pygame
import sys
import math


pygame.init()

screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Game")

background = pygame.image.load("SPRITES\\background.png").convert()
background = pygame.transform.scale(background, (1080, 720))

Bow = pygame.image.load("SPRITES\\Bow.png").convert_alpha()
scaled_bow = pygame.transform.scale(Bow, (149, 335))

bow_x = 100
bow_y = 350
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




    mouse_x, mouse_y = pygame.mouse.get_pos()


    mouse_buttons = pygame.mouse.get_pressed()
    if not mouse_buttons[2]:
        dx, dy = mouse_x - bow_x, mouse_y - bow_y
        angle = math.degrees(math.atan2(-dy, dx))


    rotated_bow = pygame.transform.rotate(scaled_bow, angle)

    bow_rect = rotated_bow.get_rect(center=(bow_x, bow_y))
    #draws the background
    screen.blit(background, (0, 0))
    #draws the bow
    screen.blit(rotated_bow, bow_rect)
    pygame.display.flip()

