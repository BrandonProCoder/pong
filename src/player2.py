import pygame
from config import *


class Player2(pygame.sprite.Sprite):

    def __init__(self, color, screen):
        super().__init__()
        self.x, self.y = 0, 0
        self.screen = screen
        self.color = color
        self.pong_board1 = pygame.image.load("assets/pong_board1.png")
        self.pong_board1 = pygame.transform.scale(self.pong_board1
                                                  , (self.resize_per(self.pong_board1.get_width(), 500)
                                                     , self.resize_per(self.pong_board1.get_height(), 500*2)))
        self.pong_board0 = pygame.image.load("assets/pong_board0.png")
        self.pong_board0 = pygame.transform.scale(self.pong_board0
                                                  , (self.resize_per(self.pong_board0.get_width(), 500)
                                                     , self.resize_per(self.pong_board0.get_height(), 500*2)))

        self.pong_boards = self.pong_board1

        self.rect = pygame.Rect(self.x, self.y, self.pong_boards.get_width(), self.pong_boards.get_height())

        self.x, self.y = self.blit_mid("x", self.pong_boards.get_width()) \
            , self.blit_mid("y", self.pong_boards.get_height())

        self.distance = 850

        self.speed = SPEED

        self.use_ai = False
        self.ai_despeed = 2

        self.ball_y = 0

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
        if self.pong_boards == self.pong_board1:
            self.pong_boards = self.pong_board0
        elif self.pong_boards == self.pong_board0:
            self.pong_boards = self.pong_board1

    def reset(self):
        self.pong_boards = self.pong_board1
        self.x, self.y = self.blit_mid("x", self.pong_boards.get_width()) \
            , self.blit_mid("y", self.pong_boards.get_height())

        self.speed = 7

    def update(self):
        key_pressed = pygame.key.get_pressed()

        mouse_x, mouse_y = pygame.mouse.get_pos()
        # self.y = mouse_y - (self.pong_boards.get_height() / 2)

        if not self.use_ai:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_UP]:
                self.y -= self.speed
            if key_pressed[pygame.K_DOWN]:
                self.y += self.speed

            if self.y <= 0:
                self.y += self.speed
            if (self.y + self.pong_boards.get_height()) >= HEIGHT:
                self.y -= self.speed
        elif self.use_ai:
            if (self.y + (self.pong_boards.get_height() / 2)) > self.ball_y:
                self.y -= (self.speed - self.ai_despeed)
            if (self.y + (self.pong_boards.get_height() / 2)) < self.ball_y:
                self.y += (self.speed - self.ai_despeed)

        self.screen.blit(self.pong_boards, (self.x + self.distance, self.y))

        self.rect.x = self.x + self.distance
        self.rect.y = self.y

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)

            pygame.draw.rect(self.screen, (255, 0, 255), (self.x + self.distance, self.y, 400, 400))
