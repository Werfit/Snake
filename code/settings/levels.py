from copy import deepcopy

from .config import APPLE_BLOCK_SIZE, BLOCK_SIZE, APPLE_LIFE_TIME, FPS
from ..logs.logger import Logger


class Level:
    __level_options = {"EASY": 1, "MIDDLE": 2, "HARD": 3}

    def __init__(self):
        self.__difficulty = "EASY"
        self.__default_values = self.__restore_default_values()

    def __restore_default_values(self):
        return {"apple_block_size": APPLE_BLOCK_SIZE, "fps": FPS, "apple_life_time": APPLE_LIFE_TIME}

    @property
    def difficulty(self):
        return self.__difficulty

    @difficulty.setter
    def difficulty(self, value):
        if value not in self.__level_options:
            raise Exception("No such level")

        self.__difficulty = value
        self.__default_values = self.__restore_default_values()

        self.__default_values["apple_block_size"] = BLOCK_SIZE if self.difficulty == "HARD" else APPLE_BLOCK_SIZE
        self.__default_values["apple_life_time"] //= self.__level_options[value]
        self.__default_values["fps"] *= self.__level_options[value]

    @property
    def settings(self):
        return self.__default_values

    def increase_fps(self, value):
        self.__default_values["fps"] += value
        Logger.write(f"[levels.py] FPS increased to {self.settings['fps']}. Delta {value}")

    def decrease_apple_life_time(self, value):
        self.__default_values["apple_life_time"] -= value
        Logger.write(f"[levels.py] ALT(Apple Life Time) decreased to {self.settings['apple_life_time']}. Delta {value}")
