import pygame
from config import *


class StartButton(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.x, self.y = 0, 0
        self.screen = screen
        self.start_button = pygame.image.load("assets/start_button.png")
        self.start_button = pygame.transform.scale(self.start_button
                                                   , (self.resize_per(self.start_button.get_width(), 800)
                                                     , self.resize_per(self.start_button.get_height(), 800)))

        self.rect = pygame.Rect(self.x, self.y, self.start_button.get_width(), self.start_button.get_height())

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

        self.x, self.y = self.blit_mid("x", self.start_button.get_width()) \
            , self.blit_mid("y", self.start_button.get_height())
        self.screen.blit(self.start_button, (self.x, self.y+300))

        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
