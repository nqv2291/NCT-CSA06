import pygame, sys

from data.prepare import *

class Controller:

    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(caption)

        self.objects = pygame.sprite.Group()
    
    def set_objects(self, ball, left_player, right_player):
        self.objects.add(ball, left_player, right_player)

        left_player.set_position(20, screen_height/2)
        right_player.set_position(screen_width-20, screen_height/2)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw_screen(self):
        self.screen.fill(bg_color)
        pygame.draw.rect(self.screen, obj_color, (screen_width/2 - 2, 0, 4, screen_height))
        self.objects.draw(self.screen)

        pygame.display.flip()
        self.clock.tick(60)
    
    def update(self):
        self.objects.update()

