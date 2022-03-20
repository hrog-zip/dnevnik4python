import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()

# https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/
class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    green = '\x1b[38;5;2m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.green + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

formatter = CustomFormatter('[ %(asctime)s ][ %(name)s ][ %(levelname)-8s ] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

from .dnevnikru import Diary
from .exceptions import *
