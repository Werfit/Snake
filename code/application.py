import pygame

from .game import Game
from .bootstrap import Bootstrap

from .settings.config import WINDOW_SIZE, WINDOW_COLOR
from .settings.levels import Level

from .logs.logger import Logger


class Application:
    over = False

    def __init__(self):
        pygame.init()
        Logger.start()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        self.level = Level()

        self.bootstrap = Bootstrap(self.screen, level=self.level)
        self.game = Game(self.screen, board=self.bootstrap.get_board(), level=self.level)

    def __listen_events(self):
        """
        Listen events and react
        """
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                self.__quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.__quit()
                if event.key == pygame.K_SPACE and self.game.over:
                    self.__restart()

            self.game.listen_events(event)
            self.bootstrap.listen_events(event, self.game.BUTTON_CALLBACKS)

    def __restart(self):
        """
        Restart game
        """
        self.game.restart()
        self.bootstrap.restart()

        Logger.write("[application.py] Game restarted")

    def __draw(self):
        """
        Draw game elements
        """
        self.screen.fill(WINDOW_COLOR)

        self.game.run()
        self.bootstrap.run()

        pygame.display.flip()

    def __quit(self):
        Logger.finish()
        self.over = True

    def run(self):
        while not self.over:
            self.__listen_events()
            self.__draw()
