from object import *
import pygame
from pygame.locals import *
import sys
# sys.path.append('object.py')
from create import *

# General setup
pygame.init()
clock = pygame.time.Clock()

# Add main objects
paddle1 = Paddle(paddle_offset, screen_height/2 - paddle_height / 2,
                 paddle_width, paddle_height, paddle_speed, K_w, K_s)
paddle2 = Paddle(screen_width - paddle_offset - paddle_width, screen_height/2 -
                 paddle_height / 2, paddle_width, paddle_height, paddle_speed, K_UP, K_DOWN)
ball = Ball(screen_width / 2 - ball_radius / 2, screen_height / 2 -
            ball_radius / 2, ball_radius, ball_speed_x, ball_speed_y)

while True:
    # Handling Input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Movements
        if event.type == KEYDOWN:
            paddle1.change_speed(event.key)
            paddle2.change_speed(event.key)
        if event.type == KEYUP:
            paddle1.restore_speed(event.key)
            paddle2.restore_speed(event.key)

    paddle1.move_paddle()
    paddle2.move_paddle()
    ball.move_ball(paddle1, paddle_width + paddle_offset)
    ball.move_ball(paddle2, paddle_width + paddle_offset)

    # Visuals
    screen.fill(bg_color)
    pygame.draw.aaline(screen, object_color, (screen_width /
                       2, 0), (screen_width/2, screen_height))
    ball.draw_score(30)
    ball.draw_timer()
    paddle1.draw_paddle()
    paddle2.draw_paddle()
    ball.draw_ball()

    # Updating the windows
    pygame.display.flip()
    clock.tick(60)
