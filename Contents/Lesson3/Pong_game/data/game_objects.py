import pygame

from data.prepare import *

class Block(pygame.sprite.Sprite):
    
    def __init__(self, path):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

class Ball(Block):

    def __init__(self):
        super().__init__(path_ball)
        self.speed_x = speed_ball_x
        self.speed_y = speed_ball_y
        self.rect.center = (screen_width/2, screen_height/2)
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.__process_screen_constraints()

    def __process_screen_constraints(self):
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.speed_y *= -1
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

class Paddle(Block):
    
    def __init__(self, speed):
        super().__init__(path_paddle)
        self.speed = speed
        self.movement = 0
    
    def update(self):
        self.rect.y += self.movement
    
    def set_position(self, x, y):
        self.rect.center = (x, y)


