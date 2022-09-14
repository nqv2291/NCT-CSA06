import pygame
from pygame.locals import *

# Creating constants
bg_color = pygame.Color('grey12')
object_color = (200, 200, 200)
paddle_width = 20
paddle_height = 140
paddle_offset = 20
paddle_speed = 7
ball_radius = 40
ball_speed_x = 5
ball_speed_y = 5

# Setting up the main window
pygame.font.init()
screen_width = 1200
screen_height = 675
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption('Pong')
font = pygame.font.Font("open_sans_regular.ttf", 80)
font2 = pygame.font.Font('open_sans_bold.ttf', 300)
