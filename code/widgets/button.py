import pygame

from ..settings.config import BUTTONS_BACKGROUND_COLOR, BUTTONS_FOREIGN_COLOR
from ..logs.logger import Logger


class Button:
    def __init__(self, text, screen, position=(0, 0), width=None):
        self.screen = screen

        self.font = pygame.font.SysFont("Arial", 20)
        self.text = text

        Logger.write(f"[button.py] Button `{text}` generated")

        self.__render_text(position, width)

    def __render_text(self, position, width):
        text = self.font.render(self.text, 1, BUTTONS_FOREIGN_COLOR)
        size = text.get_size()

        background_size = width * 2 if width else size[0] * 2, size[1] * 2

        self.surface = pygame.Surface(background_size)
        self.surface.fill(BUTTONS_BACKGROUND_COLOR)

        text_position = (
            width - size[0] // 2 if width else size[0] // 2,
            size[1] // 2
        )
        self.surface.blit(text, text_position)

        self.rect = pygame.Rect(position, background_size)

    def click(self, position, cb=lambda: print("hi")):
        mouse_x, mouse_y = position
        Logger.write(f"[button.py] Button `{self.text}` clicked")

        if not self.rect.left <= mouse_x <= self.rect.right:
            return

        if not self.rect.top <= mouse_y <= self.rect.bottom:
            return

        cb()

    def move(self, x=0, y=0):
        self.rect.x += x
        self.rect.y += y

    def center(self):
        screen_rect = self.screen.get_rect()
        self.rect.center = screen_rect.width // 2, screen_rect.height // 2

    def draw(self):
        self.screen.blit(self.surface, self.rect)
