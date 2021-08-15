import time
import pygame

from .settings.config import APPLE_DELAY_TIME
from .logs.logger import Logger

from .sprites.snake import Snake
from .sprites.apple import Apple


class Game:
    """
    Class is responsible for gameplay
    """
    over = True

    __clock = pygame.time.Clock()
    __apple = None
    __player = None

    def __init__(self, screen, board, level):
        self.screen = screen
        self.board = board
        self.level = level

        pygame.display.set_caption('Snake')

        self.board.set_hardness_growing(self.level)

        self.BUTTON_CALLBACKS = {
            "hard": self.__difficulty_decorator("HARD"),
            "middle": self.__difficulty_decorator("MIDDLE"),
            "easy": self.__difficulty_decorator("EASY"),
        }

    def __listen_keydown_events(self, key):
        if key in {pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_a}:
            self.__player.move(key)

    def __update_screen(self):
        if self.__player:
            self.__player.draw(cb=self.__finish)

        if self.__apple:
            self.__apple.draw()

    def __generate_apples(self):
        current_time = time.time()
        delay = current_time - self.start_time

        if self.__apple and self.__apple.time_to_die(self.level.settings["apple_life_time"]):
            del self.__apple
            self.__generate_apples()

        if not self.__apple and delay >= APPLE_DELAY_TIME:
            self.start_time = time.time()
            self.__apple = Apple(
                self.screen,
                size=self.level.settings["apple_block_size"]
            )

    def __check_apple_collision(self):
        if not self.__apple or not self.__player:
            return

        collided = pygame.sprite.collide_rect(self.__apple, self.__player)
        if collided:
            del self.__apple
            self.__player.extend()
            self.board.score += 1

    def __check_collisions(self):
        self.__check_apple_collision()
        if self.__player.check_head_collision():
            self.__finish()

    def __difficulty_decorator(self, level):
        """
        Starts game and sets up difficulty depending on clicked button
        """
        def __difficulty_cb():
            self.level.difficulty = level
            self.__start()
        return __difficulty_cb

    def __start(self):
        self.__player = Snake(
            self.screen,
            over=self.over,
            level=self.level.difficulty
        )

        self.start_time = time.time()
        self.over = False

    def __finish(self):
        Logger.write("[game.py] Game finished")
        self.over = True
        self.__player = None

    def restart(self):
        self.__player = None
        self.__apple = None
        self.board.score = 0

    def listen_events(self, event):
        if event.type == pygame.KEYDOWN and not self.over:
            self.__listen_keydown_events(event.key)

    def run(self):
        if not self.over:
            self.__generate_apples()
            self.__check_collisions()
            self.__update_screen()
            self.__clock.tick(self.level.settings["fps"])
