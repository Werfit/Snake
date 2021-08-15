from random import randint
from .settings.config import WINDOW_SIZE


def find_position(block_size):
    win_size = WINDOW_SIZE[0] // block_size[0] - 1, WINDOW_SIZE[1] // block_size[1] - 1
    position = (randint(0, win_size[0]) * block_size[0],
                randint(0, win_size[1]) * block_size[1])
    return position
