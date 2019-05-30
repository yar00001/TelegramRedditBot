import logging
import os


def get_configured_logger(name="__name__", file="info.log"):
    """
    :param name: log name
    :param file: log file name.
    :return: return a logger with
    """

    dir_name = os.path.dirname(file)
    if dir_name:
        os.makedirs(file, exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # start save files from Debug level
    fh = logging.FileHandler(file)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    return logger
