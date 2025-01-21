import pygame
from config import *


class Scoreboard(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen

        self.score_font = pygame.font.SysFont("Oswald", 100)

        self.player1_score = 0

        self.player2_score = 0

        self.color = BLACK

    def opposite_color(self, color):
        if color == BLACK:
            return WHITE
        elif color == WHITE:
            return BLACK

    def update(self):

        score_text = self.score_font.render(f"{self.player1_score} | {self.player2_score}", True
                                            , self.opposite_color(self.color))
        self.screen.blit(score_text, (WIDTH_MIDDLE - (score_text.get_width() / 2), 50))
