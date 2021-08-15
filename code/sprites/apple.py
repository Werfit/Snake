import time
from datetime import datetime
import pygame

from ..settings.config import APPLE_BLOCK_SIZE, APPLE_COLOR
from ..utils import find_position

from ..logs.logger import Logger


class Apple(pygame.sprite.Sprite):
    def __init__(self, screen, pos=None, size=APPLE_BLOCK_SIZE):
        super().__init__()
        self.screen = screen

        position = pos or find_position(size)
        self.rect = pygame.Rect(position, size)

        self.start_time = time.time()

        Logger.write("[apple.py] Apple generated")

        self.generated = datetime.now()

    def time_to_die(self, life_time):
        tm = time.time()
        return tm - self.start_time >= life_time

    def draw(self):
        pygame.draw.rect(self.screen, APPLE_COLOR, self.rect)
