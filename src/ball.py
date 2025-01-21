import pygame
import random
from config import *


class Ball(pygame.sprite.Sprite):

    def __init__(self, side, color, screen, player1rect, player2rect, powerup_rect):
        super().__init__()
        self.x, self.y = 0, 0
        self.side = side
        self.screen = screen
        self.color = color
        self.player1rect = player1rect
        self.player2rect = player2rect
        self.powerup_rect = powerup_rect
        self.ball1 = pygame.image.load("assets/ball1.png")
        self.ball1 = pygame.transform.scale(self.ball1
                                            , (self.resize_per(self.ball1.get_width(), 500)
                                               , self.resize_per(self.ball1.get_height(), 500)))
        self.ball0 = pygame.image.load("assets/ball0.png")
        self.ball0 = pygame.transform.scale(self.ball0
                                            , (self.resize_per(self.ball0.get_width(), 500)
                                               , self.resize_per(self.ball0.get_height(), 500)))

        # fireball

        self.fire_ball1 = pygame.image.load("assets/fire_ball1.png")
        self.fire_ball1 = pygame.transform.scale(self.fire_ball1
                                                 , (self.resize_per(self.fire_ball1.get_width(), 300)
                                                    , self.resize_per(self.fire_ball1.get_height(), 300)))
        self.fire_ball0 = pygame.image.load("assets/fire_ball0.png")
        self.fire_ball0 = pygame.transform.scale(self.fire_ball0
                                                 , (self.resize_per(self.fire_ball0.get_width(), 300)
                                                    , self.resize_per(self.fire_ball0.get_height(), 300)))

        self.balls = self.ball1

        self.rect = pygame.Rect(self.x, self.y, self.balls.get_width(), self.balls.get_height())

        self.x, self.y = self.blit_mid("x", self.balls.get_width()) \
            , self.blit_mid("y", self.balls.get_height())

        self.status = ALIVE

        self.sides = ["left", "right"]

        self.color_switch = False
        self.speed = SPEED

        self.bounce_speed = 0
        self.bounce_slope = random.randint(2 + self.bounce_speed, 5 + self.bounce_speed)

        # 2 types, normal/fire

        self.ball_type = "normal"
        self.fire_ball_speed = 0

        self.player1_score = 0
        self.player2_score = 0

    def resize_per(self, dimension, percent):
        size = dimension * (percent / 100)
        return size

    def blit_mid(self, axis, dimension):
        if axis == "y":
            middle = HEIGHT_MIDDLE - (dimension / 2)
            return middle
        if axis == "x":
            middle = WIDTH_MIDDLE - (dimension / 2)
            return middle

    def swap_color(self):
        if self.ball_type == "normal":
            if self.balls == self.ball1:
                self.balls = self.ball0
            elif self.balls == self.ball0:
                self.balls = self.ball1

    def handle_board_collision(self, player1, player2, powerup_rect):
        if self.rect.colliderect(player1):
            if self.color == BLACK:
                self.balls = self.ball1
            if self.color == WHITE:
                self.balls = self.ball0

            self.player1_score += 1

            self.side = "right"
            self.ball_type = "normal"

            self.color_switch = True

            return True

        if self.rect.colliderect(player2):
            if self.color == BLACK:
                self.balls = self.ball1
            if self.color == WHITE:
                self.balls = self.ball0

            self.player2_score += 1

            self.side = "left"
            self.ball_type = "normal"

            self.color_switch = True

            return True

        if self.rect.colliderect(powerup_rect):
            bro = 3
            '''self.ball_type = "fire"'''
        else:
            return False

    def reset(self):
        self.side = random.choice(self.sides)
        if self.ball_type == "normal":
            self.balls = self.ball1
        elif self.ball_type == "fire":
            pass
            # self.balls = self.fire_ball1
        self.x, self.y = self.blit_mid("x", self.balls.get_width()) \
            , self.blit_mid("y", self.balls.get_height())

        self.speed = 5
        self.bounce_speed = 0

        self.player1_score = 0
        self.player2_score = 0

        self.ball_type = "normal"

    def bounce(self):
        self.bounce_slope = random.randint(2, 20) + self.bounce_speed

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_e]:
            self.ball_type = "fire"

        if self.ball_type == "fire":
            self.fire_ball_speed = 7
        else:
            self.fire_ball_speed = 0

        self.rect = pygame.Rect(self.x, self.y, self.balls.get_width(), self.balls.get_height())

        if self.x <= 0 or self.x >= WIDTH:
            self.status = DEAD

        if self.y <= 0 or (self.y + self.balls.get_height()) >= HEIGHT:
            if (self.y + self.balls.get_height()) >= HEIGHT:
                self.bounce_slope = -self.bounce_slope
            if self.y <= 0:
                self.bounce_slope = -self.bounce_slope

        self.screen.blit(self.balls, (self.x, self.y))

        self.handle_board_collision(self.player1rect, self.player2rect, self.powerup_rect)

        if self.side == "right":
            self.x += self.speed + self.fire_ball_speed
            self.y += self.bounce_slope
            if self.ball_type == "fire":
                self.balls = self.fire_ball0
        if self.side == "left":
            self.x -= self.speed + self.fire_ball_speed
            self.y += self.bounce_slope
            if self.ball_type == "fire":
                self.balls = self.fire_ball1

        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.player1rect)
            pygame.draw.rect(self.screen, (255, 0, 255), self.player2rect)
            pygame.draw.rect(self.screen, (255, 0, 255), self.powerup_rect)

            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
