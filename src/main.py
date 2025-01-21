import pygame
from config import *
from startButton import StartButton
from player1 import Player1
from player2 import Player2
from ball import Ball
from player1AiButton import Player1AiButton
from player2AiButton import Player2AiButton
from exitSign import ExitSign
from scoreboard import Scoreboard
from powerUps import PowerUps
import random


class Pong:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
        self.project_name = 'Pong'

        # Running game name
        pygame.display.set_caption(self.project_name)

        # Loop until the user clicks the close button.
        self.running = True

        # Used to manage how fast the screen updates
        self.clock = pygame.time.Clock()

        # ________Text________
        self.FPS_font = pygame.font.SysFont("Arial", 15)

        # Images

        # Groups

        self.start_button_group = pygame.sprite.Group()
        self.player1_group = pygame.sprite.Group()
        self.player2_group = pygame.sprite.Group()
        self.player1_ai_button_group = pygame.sprite.Group()
        self.player2_ai_button_group = pygame.sprite.Group()
        self.ball_group = pygame.sprite.Group()
        self.exit_sign_group = pygame.sprite.Group()
        self.scoreboard_group = pygame.sprite.Group()
        self.powerup_group = pygame.sprite.Group()

        # Variables

        self.x, self.y = 0, 0
        self.event = 0
        self.color = WHITE

        self.exit_on = False
        self.exit_off = False
        self.exit_timer = 0
        self.exit_Time = 5
        self.exit_on_num = 0

        self.current_fps = str(self.clock.get_fps())
        self.fps_text = self.FPS_font.render(f"FPS {self.current_fps}", True, RED)

        # Group add

        self.start_button = StartButton(self.screen)
        self.start_button_group.add(self.start_button)

        self.player1_ai_button = Player1AiButton(self.screen)
        self.player1_ai_button_group.add(self.player1_ai_button)

        self.player2_ai_button = Player2AiButton(self.screen)
        self.player2_ai_button_group.add(self.player2_ai_button)

        self.player1 = Player1(self.color, self.screen)
        self.player1_group.add(self.player1)

        self.player2 = Player2(self.color, self.screen)
        self.player2_group.add(self.player2)

        self.scoreboard = Scoreboard(self.screen)
        self.scoreboard_group.add(self.scoreboard)

        self.powerup = PowerUps(WIDTH_MIDDLE, HEIGHT_MIDDLE, self.screen)
        self.powerup_group.add(self.powerup)

        self.side = ["left", "right"]
        self.side_choice = random.choice(self.side)
        self.ball = Ball(self.side_choice, self.color, self.screen, self.player1.rect, self.player2.rect
                         , self.powerup.rect)

        self.exit_sign = ExitSign(self.screen)
        self.exit_sign_group.add(self.exit_sign)

        self.timer = 0
        self.timed = 50

        # notes

    def create_FPS_Text(self):
        bro = False
        '''self.current_fps = str(self.clock.get_fps())
        self.screen.blit(self.fps_text, (15, 15))'''

    def color_swap(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE

    def exit_button_clicked(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.exit_sign.rect.collidepoint(mouse_x, mouse_y):
            self.running = False
            pygame.quit()

    def toggle_exit_menu(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE] and self.exit_on and self.exit_on_num >= 1:
            self.exit_on_num = 0
            self.exit_on = False
            self.exit_off = True
        if not key_pressed[pygame.K_ESCAPE] and self.exit_off and self.exit_on_num <= 0:
            self.exit_off = False
        elif key_pressed[pygame.K_ESCAPE] and not self.exit_off:
            self.exit_on_num += 1
            self.exit_on = False
        if self.exit_on_num >= 1:
            self.exit_sign_group.update()
            self.exit_button_clicked()
        if not key_pressed[pygame.K_ESCAPE] and self.exit_on_num >= 1 and not self.exit_on:
            self.exit_on = True

    def game_loop(self):
        # -------- Main Program Loop -----------
        while self.running:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()
            # Below is how you draw self.background on the screen

            self.screen.fill(self.color)
            key_pressed = pygame.key.get_pressed()

            if self.event == START_SCREEN:
                # ai playing in menu
                self.create_FPS_Text()

                self.player1.use_ai = True
                self.player2.use_ai = True

                self.player1.ai_despeed = 0
                self.player2.ai_despeed = 0

                self.player1_group.update()
                self.player2_group.update()
                self.ball.update()
                self.player1.ball_y = self.ball.y
                self.player2.ball_y = self.ball.y

                self.start_button_group.update()
                self.player1_ai_button_group.update()
                self.player2_ai_button_group.update()

                self.player1.pong_boards = self.player1.pong_board0
                self.player2.pong_boards = self.player2.pong_board0
                self.ball.balls = self.ball.ball0

                self.color = WHITE
                if key_pressed[pygame.K_SPACE] or self.player1_ai_button.start_game or self.player2_ai_button.start_game:

                    if self.player1_ai_button.start_game:
                        self.player1.use_ai = True
                        self.player2.use_ai = False
                    elif self.player2_ai_button.start_game:
                        self.player1.use_ai = False
                        self.player2.use_ai = True

                    if not self.player1_ai_button.start_game and not self.player2_ai_button.start_game:
                        self.player1.use_ai = False
                        self.player2.use_ai = False

                    self.event = GAME_STARTS

            elif self.event == GAME_STARTS:

                self.create_FPS_Text()
                self.color = BLACK
                self.ball.balls = self.ball.ball1

                self.player1.ai_despeed = 2
                self.player2.ai_despeed = 2

                # player things
                self.player1.reset()
                self.player2.reset()
                # ball things
                self.ball.reset()
                self.ball.status = ALIVE
                self.ball_group.add(self.ball)

                self.event = GAME_STARTED
                self.powerup.hit = False

            elif self.event == GAME_STARTED:
                self.timer += 1
                if self.timer >= self.timed:
                    pass
                    '''self.powerup.ball_rect = self.ball.rect
                    self.powerup.hit = False'''

                    if not self.powerup.hit:
                        pass
                        # self.powerup_group.update()

                self.create_FPS_Text()

                self.powerup.hit = False
                self.powerup.ball_rect = None

                self.powerup.color = self.color

                self.ball.color = self.color

                self.scoreboard_group.update()
                self.scoreboard.color = self.color

                self.scoreboard.player1_score = self.ball.player1_score
                self.scoreboard.player2_score = self.ball.player2_score

                self.player1_group.update()
                self.player2_group.update()
                self.ball.update()
                self.player1.ball_y = self.ball.y
                self.player2.ball_y = self.ball.y
                if self.ball.color_switch:
                    self.color_swap()
                    self.ball.swap_color()
                    self.player1.swap_color()
                    self.player2.swap_color()
                    self.ball.color_switch = False

                    # increase speed
                    self.ball.bounce_speed += 0.10
                    self.ball.speed += 0.20
                    self.player1.speed += 0.1
                    self.player2.speed += 0.1
                if self.ball.status == DEAD:
                    self.event = GAME_ENDED
                    self.ball.kill()
            elif self.event == GAME_ENDED:
                self.player1.use_ai = False
                self.player2.use_ai = False
                self.player1_ai_button.start_game = False
                self.player2_ai_button.start_game = False

                # reset for menu screen
                self.player1.reset()
                self.player2.reset()
                self.ball.reset()
                self.ball.status = ALIVE
                self.ball_group.add(self.ball)

                self.event = START_SCREEN

                self.create_FPS_Text()

            self.toggle_exit_menu()
            self.exit_sign.color = self.color
            self.create_FPS_Text()

            # --- Limit to fps_num frames per second

            self.clock.tick(FPS)
            pygame.display.set_caption(f'{self.project_name} DEMO')

        # Close the window and quit.
        pygame.quit()


if __name__ == '__main__':
    sb = Pong()
    sb.game_loop()
