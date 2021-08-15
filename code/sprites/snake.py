import pygame

from ..settings.config import WINDOW_SIZE, BLOCK_SIZE, PLAYER_COLOR, PLAYER_SPEED, DEFAULT_TAIL_LEN, TAIL_COLOR
from ..utils import find_position
from ..logs.logger import Logger

from .block import Block


class Snake(pygame.sprite.Sprite):
    __direction = [0, 0]
    __tail = pygame.sprite.Group()
    __direction_change_allowed = True

    def __init__(self, screen, pos=None, level="easy", over=False):
        super().__init__()
        position = pos or find_position(BLOCK_SIZE)

        self.screen = screen
        self.level = level
        self.rect = pygame.Rect(position, BLOCK_SIZE)
        self.over = over

        self.__fill_tail(position)
        Logger.write("[snake.py] Snake generated")

    def __fill_tail(self, position):
        """
        Creates tail with default len for snake
        """
        for i in range(DEFAULT_TAIL_LEN):
            self.__tail.add(Block(
                self.screen,
                (position[0], position[1] + (i + 1) * BLOCK_SIZE[1])
            ))

        Logger.write("[snake.py] Snake tail generated")

    def __update_tail(self):
        """
        Updates tail position every move
        """
        tail = self.__tail.sprites()

        index = len(tail) - 1
        while index >= 0:
            tail[index].rect.topleft = tail[index - 1].rect.topleft if index else self.rect.topleft
            index -= 1

    def __update(self, cb):
        """
        Update player position every move
        """
        next_x = self.rect[0] + PLAYER_SPEED * self.__direction[0]
        next_y = self.rect[1] + PLAYER_SPEED * self.__direction[1]

        if self.level != "EASY":
            if next_x < 0 or next_y < 0 \
                    or WINDOW_SIZE[0] <= next_x or WINDOW_SIZE[1] <= next_y:
                cb()
                return

        if next_x < 0:
            next_x = WINDOW_SIZE[0] - BLOCK_SIZE[0]
        if next_y < 0:
            next_y = WINDOW_SIZE[1] - BLOCK_SIZE[1]

        if next_x >= WINDOW_SIZE[0]:
            next_x = 0
        if next_y >= WINDOW_SIZE[1]:
            next_y = 0

        if self.__direction != [0, 0]:
            self.__update_tail()
        self.rect.x, self.rect.y = next_x, next_y

    def __draw_tail(self):
        """
        Draws tail
        """
        for index, block in enumerate(self.__tail):
            i = index if index < len(TAIL_COLOR) else -1
            block.draw(TAIL_COLOR[i])

    def check_head_collision(self):
        """
        Check collisions
        """
        collision = pygame.sprite.spritecollideany(self, self.__tail)
        if collision:
            Logger.write("[snake.py] Snake collided its tail")
        return collision

    def extend(self):
        """
        Add block to snake's tail
        """
        last_block = self.__tail.sprites()[-1]
        self.__tail.add(Block(self.screen, last_block.rect.topleft))
        Logger.write("[snake.py] Tail extended")

    def move(self, key):
        """
        Change snake's direction according to key
        """
        if not self.__direction_change_allowed:
            return

        if key == pygame.K_w and self.__direction[1] != 1:
            self.__direction = [0, -1]
            self.__direction_change_allowed = False
        elif key == pygame.K_d and self.__direction[0] != -1:
            self.__direction = [1, 0]
            self.__direction_change_allowed = False
        elif key == pygame.K_s and self.__direction[1] != -1 and self.__direction != [0, 0]:
            self.__direction = [0, 1]
            self.__direction_change_allowed = False
        elif key == pygame.K_a and self.__direction[0] != 1:
            self.__direction = [-1, 0]
            self.__direction_change_allowed = False

    def draw(self, cb):
        """
        Draw snake
        """
        self.__update(cb)
        self.__draw_tail()
        pygame.draw.rect(self.screen, PLAYER_COLOR, self.rect)

        self.__direction_change_allowed = True

    def __del__(self):
        """
        Set snake fields to defaults in order to avoid id errors
        """
        self.__tail.empty()
        self.__direction = [0, 0]
