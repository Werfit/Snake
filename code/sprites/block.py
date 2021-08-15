import pygame

from ..settings.config import BLOCK_SIZE


class Block(pygame.sprite.Sprite):
    def __init__(self, screen, pos=(0, 0)):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(pos, BLOCK_SIZE)

    def draw(self, color):
        pygame.draw.rect(self.screen, color, self.rect)