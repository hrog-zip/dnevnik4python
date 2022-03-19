import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

from .dnevnikru import Diary
from .exceptions import *
