import pygame

from data.game_controller import Controller
from data.game_objects import *


def game():
    pygame.init()
    pygame.display.set_caption("Pong game v2.1")

    pygame.mixer.init()

    controller = Controller()

    ball = Ball()
    player = Player(speed_player, pygame.K_w, pygame.K_s)
    player2 = Player(speed_player, pygame.K_UP, pygame.K_DOWN)
    # opponent = VirtualPlayer(speed_virtual_player, ball)

    controller.set_objects(ball, player, player2)
    

    while True:
        controller.check_events()
        controller.update()
        controller.draw_screen()

if __name__ == '__main__':
    game()
