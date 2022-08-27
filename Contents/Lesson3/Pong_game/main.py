import pygame

from data.prepare import *
from data.game_objects import *
from data.game_controller import Controller

# initial setup
pygame.init()

controller = Controller()

ball = Ball()
p1 = Paddle(speed_player)
p2 = Paddle(speed_player)

controller.set_objects(ball, p1, p2)


while True:
    
    controller.check_events()
    controller.draw_screen()
    controller.update()
    
    

