import pygame, sys

from prepare import *

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255, 255, 255))
    
    pygame.display.flip()
    clock.tick(60)
