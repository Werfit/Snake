import pygame

from .settings.config import BUTTON_PADDING
from .widgets.button import Button
from .widgets.board import Board


class Bootstrap:
    """
    Class is responsible for buttons and board
    """
    visible = True

    def __init__(self, screen, level):
        self.__board = Board(screen)
        self.__hard_button = Button(screen=screen, width=200, text="Hard")
        self.__middle_button = Button(screen=screen, width=200, text="Middle")
        self.__easy_button = Button(screen=screen, width=200, text="Easy")

        self.__hard_button.center()
        self.__middle_button.center()
        self.__easy_button.center()

        self.__hard_button.move(y=-(self.__hard_button.rect.height + BUTTON_PADDING))
        self.__easy_button.move(y=self.__easy_button.rect.height + BUTTON_PADDING)

        self.level = level

    def __bootstrap_callback(self, cb):
        def wrapper():
            self.visible = False
            cb()
        return wrapper

    def __draw(self):
        self.__hard_button.draw()
        self.__middle_button.draw()
        self.__easy_button.draw()

    def restart(self):
        self.visible = True

    def listen_events(self, event, cb):
        if event.type == pygame.MOUSEBUTTONDOWN and self.visible:
            self.__hard_button.click(
                pygame.mouse.get_pos(),
                cb=self.__bootstrap_callback(cb["hard"])
            )
            self.__middle_button.click(
                pygame.mouse.get_pos(),
                cb=self.__bootstrap_callback(cb["middle"])
            )
            self.__easy_button.click(
                pygame.mouse.get_pos(),
                cb=self.__bootstrap_callback(cb["easy"])
            )

    def get_board(self):
        return self.__board

    def run(self):
        if self.visible:
            self.__draw()
        else:
            self.__board.draw()
