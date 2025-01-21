import pygame
from config import *


class PowerUps(pygame.sprite.Sprite):

    def __init__(self, x, y, screen):
        super().__init__()
        self.x, self.y = x, y
        self.screen = screen

        self.fireball_powerup0 = pygame.image.load("assets/fire_ball_powerup0.png")
        self.fireball_powerup0 = pygame.transform.scale(self.fireball_powerup0
                                                        , (self.resize_per(self.fireball_powerup0.get_width(), 600)
                                                        , self.resize_per(self.fireball_powerup0.get_height(), 600)))

        self.fireball_powerup1 = pygame.image.load("assets/fire_ball_powerup1.png")
        self.fireball_powerup1 = pygame.transform.scale(self.fireball_powerup1
                                                        , (self.resize_per(self.fireball_powerup1.get_width(), 600)
                                                        , self.resize_per(self.fireball_powerup1.get_height(), 600)))

        self.powerup = self.fireball_powerup0

        self.ball_rect = pygame.Rect(self.x, self.y, self.powerup.get_width(), self.powerup.get_height())

        self.color = WHITE

        self.rect = pygame.Rect(self.x, self.y, self.powerup.get_width(), self.powerup.get_height())

        self.hit = False

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

    def handle_board_collision(self, ball_rect):
        if self.rect.colliderect(ball_rect):
            self.hit = True
        else:
            return False

    def update(self):

        if self.color == WHITE:
            self.powerup = self.fireball_powerup0
        if self.color == BLACK:
            self.powerup = self.fireball_powerup1

        self.screen.blit(self.powerup, (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y

        self.handle_board_collision(self.ball_rect)

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
            pygame.draw.rect(self.screen, (255, 0, 255), self.ball_rect)
