import pygame
from pygame.locals import *

from create import *


class Paddle(pygame.Rect):
    def __init__(self, x, y, width, height, speed, key_move_up, key_move_down):
        super().__init__(x, y, width, height)
        self.speed = 0
        self.key_move_up = key_move_up
        self.key_move_down = key_move_down

    def change_speed(self, key_pressed):
        if key_pressed == self.key_move_up:
            self.speed = -paddle_speed
        if key_pressed == self.key_move_down:
            self.speed = paddle_speed

    def restore_speed(self, key_pressed):
        if key_pressed == self.key_move_up or key_pressed == self.key_move_down:
            self.speed = 0

    def move_paddle(self):
        self.y += self.speed
        if self.top <= -paddle_height / 2:
            self.top = -paddle_height / 2
        if self.bottom >= screen_height + paddle_height / 2:
            self.bottom = screen_height + paddle_height / 2

    def draw_paddle(self):
        pygame.draw.rect(screen, object_color, self)


class Ball(pygame.Rect):
    def __init__(self, x, y, radius, speed_x, speed_y):
        super().__init__(x, y, radius, radius)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.timer = 359
        self.score1 = 0
        self.score2 = 0

    def move_ball(self, paddle, offset):
        self.timer -= 1
        if self.timer <= 0:
            self.x += self.speed_x
            self.y += self.speed_y
        if self.top <= 0 or self.bottom >= screen_height:
            self.speed_y *= -1
        if self.left <= 0:
            self.score2 += 1
            self.timer = 359
            self.x = screen_width/2 - self.width/2
            self.y = screen_height/2 - self.height/2
        if self.right >= screen_width:
            self.score1 += 1
            self.timer = 359
            self.x = screen_width/2 - self.width/2
            self.y = screen_height/2 - self.height/2

        if self.colliderect(paddle):
            self.speed_x *= -1
            if self.x <= screen_width / 2:
                self.left = offset
            else:
                self.right = screen_width - offset

    def draw_ball(self):
        pygame.draw.ellipse(screen, object_color, self)

    def draw_timer(self):
        if self.timer > 0:
            timer_surface = font2.render(
                str(self.timer//120+1), True, (125, 125, 125))
            screen.blit(timer_surface, (screen_width/2 - timer_surface.get_width() /
                        2, screen_height/2 - timer_surface.get_height()/2))

    def draw_score(self, offset):
        score1_surface = font.render(str(self.score1), True, (255, 255, 255))
        score2_surface = font.render(str(self.score2), True, (255, 255, 255))
        screen.blit(score1_surface, (screen_width / 2 -
                    score1_surface.get_width() - offset, offset))
        screen.blit(score2_surface, (screen_width / 2 + offset, offset))
