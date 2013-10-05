import logging

LOGGING_FILE = 'evetools.log'

def init():
    logger = logging.getLogger('base')
    handler = logging.FileHandler(LOGGING_FILE)
    handler.setFormatter(logging.Formatter(
        '%(levelname)s:%(asctime)s:%(message)s', '%Y-%m-%d %H:%M:%S'))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

logger = init()
