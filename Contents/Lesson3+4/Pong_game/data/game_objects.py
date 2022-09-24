import pygame, random

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
        self.paddles = pygame.sprite.Group()
        self.counter = Counter()
        self.sound_bonk = pygame.mixer.Sound(path_sound_bonk)
        self.__reset_ball()
    
    def set_paddles(self, left_player, right_player):
        self.left_player = left_player
        self.right_player = right_player
        self.paddles.add(left_player, right_player)

    def update(self):
        if not self.counter.is_counting:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.__process_screen_constraints()
            self.__process_collisions()

    def __process_screen_constraints(self):
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            pygame.mixer.Sound.play(self.sound_bonk)
            self.speed_y *= -1
        elif self.rect.left < 0:
            self.right_player.score.add_score()
            self.__reset_ball()
        elif self.rect.right > screen_width:
            self.left_player.score.add_score()
            self.__reset_ball()
    
    def __process_collisions(self):
        if pygame.sprite.spritecollideany(self, self.paddles):
            pygame.mixer.Sound.play(self.sound_bonk)
            self.speed_x *= -1
    
    def __reset_ball(self):
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])
        self.rect.center = (screen_width/2, screen_height/2)
        self.counter.count()

class Paddle(Block):

    def __init__(self, speed):
        super().__init__(path_paddle)
        self.movement = 0
        self.speed = speed
    
    def update(self):
        self.rect.y += self.movement
        self.__process_screen_constraints()
    
    def __process_screen_constraints(self):
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
    
    def set_position(self, x, y):
        self.rect.center = (x, y)
    
    def set_score(self, x, y):
        self.score = Score(x, y)

class Player(Paddle):

    def __init__(self, speed, key_go_up, key_go_down):
        super().__init__(speed)
        self.key_go_up = key_go_up
        self.key_go_down = key_go_down
    
    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.key_go_up:
                self.movement -= self.speed
            elif event.key == self.key_go_down:
                self.movement += self.speed
        elif event.type == pygame.KEYUP:
            if event.key == self.key_go_up:
                self.movement += self.speed
            elif event.key == self.key_go_down:
                self.movement -= self.speed

class VirtualPlayer(Paddle):

    def __init__(self, speed, ball):
        super().__init__(speed)
        self.ball = ball
    
    def update(self):
        super().update()
        if self.rect.top > self.ball.rect.top:
            self.movement = -self.speed
        elif self.rect.bottom < self.ball.rect.bottom:
            self.movement = self.speed
        else:
            self.movement = 0

class Text(pygame.sprite.Sprite):
    
    def __init__(self, x, y, font_name, font_size):
        super().__init__()
        self.font = pygame.font.Font(font_name, font_size)
        self.center = (x, y)
        self.image = self.font.render("", True, obj_color, bg_color)
        self.rect = self.image.get_rect(center=self.center)

class Counter(Text):

    def __init__(self):
        super().__init__(screen_width/2, screen_height/2+40, font_name, font_size)
        self.count()

    def update(self):
        if self.is_counting:
            time_elapsed = pygame.time.get_ticks() - self.stop_time

            if time_elapsed <= 3000:
                count = self.time_limit - (time_elapsed // 1000)
                self.image = self.font.render(str(count), True, obj_color, bg_color)
                self.rect = self.image.get_rect(center=self.center)
            else:
                self.image = self.font.render("", True, obj_color, bg_color)
                self.is_counting = False
    
    def count(self):
        self.stop_time = pygame.time.get_ticks()
        self.is_counting = True
        self.time_limit = 3


class Score(Text):

    def __init__(self, x, y):
        super().__init__(x, y, font_name, font_size)
        self.value = 0
        self.sound_score = pygame.mixer.Sound(path_sound_score)

    def update(self):
        self.image = self.font.render(str(self.value), True, obj_color, bg_color)
        self.rect = self.image.get_rect(center=self.center)
    
    def add_score(self):
        pygame.mixer.Sound.play(self.sound_score)
        self.value += 1

