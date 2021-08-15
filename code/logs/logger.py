import datetime
import time


class Logger:
    __file = None

    @staticmethod
    def __get_current_time():
        tm = time.localtime()
        return f"{tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}"

    @staticmethod
    def __get_current_date():
        tm = time.localtime()
        return f"{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday}"

    @classmethod
    def start(cls):
        cls.__file = open(f"./code/logs/log-{cls.__get_current_date()}.txt", "a+")
        cls.write("[logger.py] Session started")

    @classmethod
    def write(cls, info):
        cls.__file.write(f"[{cls.__get_current_time()}] {info}\n")

    @classmethod
    def finish(cls):
        cls.write("[logger.py] Session finished")
        cls.write("-"*40)
        cls.__file.close()
