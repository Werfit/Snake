import pygame

from ..settings.config import WINDOW_SIZE, WINDOW_COLOR, SCORE_COLOR, FPS_DELTA, APPLE_LIFE_TIME_DELTA
from ..logs.logger import Logger


class Board:
    __score = 0
    __level = None

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

        if self.__level and self.__score != 0:
            if self.__score % 10 == 0 and self.__level.settings["apple_life_time"] >= APPLE_LIFE_TIME_DELTA * 0.15:
                self.__level.decrease_apple_life_time(APPLE_LIFE_TIME_DELTA)
            if self.__score % 5 == 0:
                self.__level.increase_fps(FPS_DELTA)

    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 18)

        Logger.write("[board.py] Board created")

    def __render_text(self):
        text = self.font.render(f"Score: {self.score}", 1, SCORE_COLOR)
        size = text.get_size()

        self.surface = pygame.Surface(size)
        self.surface.fill(WINDOW_COLOR)

        position = (0, 0)
        self.surface.blit(text, position)
        self.rect = pygame.Rect((WINDOW_SIZE[0] - size[0] - 40, 40), size)

    def set_hardness_growing(self, level):
        self.__level = level

        Logger.write("[board.py] Board hardness started growing")

    def draw(self):
        self.__render_text()
        self.screen.blit(self.surface, self.rect)
