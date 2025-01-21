import pygame
from config import *


class ExitSign(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.x, self.y = 0, 0
        self.screen = screen
        self.exit_sign0 = pygame.image.load("assets/exit_sign0.png")
        self.exit_sign0 = pygame.transform.scale(self.exit_sign0
                                                , (self.resize_per(self.exit_sign0.get_width(), 800)
                                                        , self.resize_per(self.exit_sign0.get_height(), 800)))

        self.exit_sign_big0 = pygame.image.load("assets/exit_sign0.png")
        self.exit_sign_big0 = pygame.transform.scale(self.exit_sign_big0
                                                , (self.resize_per(self.exit_sign_big0.get_width(), 820)
                                                        , self.resize_per(self.exit_sign_big0.get_height(), 820)))

        self.exit_sign1 = pygame.image.load("assets/exit_sign1.png")
        self.exit_sign1 = pygame.transform.scale(self.exit_sign1
                                                 , (self.resize_per(self.exit_sign1.get_width(), 800)
                                                    , self.resize_per(self.exit_sign1.get_height(), 800)))

        self.exit_sign_big1 = pygame.image.load("assets/exit_sign1.png")
        self.exit_sign_big1 = pygame.transform.scale(self.exit_sign_big1
                                                     , (self.resize_per(self.exit_sign_big1.get_width(), 820)
                                                        , self.resize_per(self.exit_sign_big1.get_height(), 820)))

        self.button0 = self.exit_sign0
        self.button1 = self.exit_sign1
        self.button_color = self.button0

        self.color = WHITE

        self.rect = pygame.Rect(self.x, self.y, self.button_color.get_width(), self.button_color.get_height())

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
        if self.color == WHITE:
            self.button_color = self.button0
        if self.color == BLACK:
            self.button_color = self.button1

        mouse_x, mouse_y = pygame.mouse.get_pos()

        if self.button_color == self.button0:
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.button0 = self.exit_sign_big0
            elif not self.rect.collidepoint(mouse_x, mouse_y):
                self.button0 = self.exit_sign0

        if self.button_color == self.button1:
            if self.rect.collidepoint(mouse_x, mouse_y):
                self.button1 = self.exit_sign_big1
            elif not self.rect.collidepoint(mouse_x, mouse_y):
                self.button1 = self.exit_sign1

        self.x, self.y = self.blit_mid("x", self.button_color.get_width()) \
            , self.blit_mid("y", self.button_color.get_height())
        self.screen.blit(self.button_color, (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y

        if DEBUG:
            pygame.draw.rect(self.screen, (255, 0, 255), self.rect)
