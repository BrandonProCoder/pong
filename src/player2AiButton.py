import pygame
from config import *


class Player2AiButton(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.x, self.y = 0, 0
        self.screen = screen
        self.start_button = pygame.image.load("assets/player2_ai.png")
        self.start_button = pygame.transform.scale(self.start_button
                                                   , (self.resize_per(self.start_button.get_width(), 800)
                                                     , self.resize_per(self.start_button.get_height(), 800)))

        self.start_button_big = pygame.transform.scale(self.start_button, (self.start_button.get_width()+15, self.start_button.get_height()+15))

        self.button = self.start_button

        self.rect = pygame.Rect(self.x, self.y, self.button.get_width(), self.button.get_height())
        self.start_game = False

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

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.button.get_width(), self.button.get_height())

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_x, mouse_y):
            self.button = self.start_button_big
            if pygame.mouse.get_pressed()[0]:
                self.start_game = True
        elif not self.rect.collidepoint(mouse_x, mouse_y):
            self.button = self.start_button

        self.x, self.y = self.blit_mid("x", self.button.get_width())+250 \
            , self.blit_mid("y", self.button.get_height())+50
        self.screen.blit(self.button, (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
