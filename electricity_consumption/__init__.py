"""electricity consumption package
This package provides functions get consumption information, and perform analyses
"""

import logging
import os


def create_logger() -> logging.Logger:
    """Create default package logger and return it.
    Returns
    -------
    logging.Logger
        default package logger
    """
    default_log_format = (
        "%(asctime)s - %(name)s - %(filename)s - %(funcName)s (%(lineno)d) - %(levelname)s : %(message)s"
    )
    default_log_datefmt = "%d/%m/%Y %H:%M:%S"
    default_log_level = "INFO"

    log_format = os.getenv("LOG_FORMAT", default_log_format)
    log_datefmt = os.getenv("LOG_DATEFMT", default_log_datefmt)
    log_level = os.getenv("LOG_LEVEL_" + __package__.upper(), default_log_level)
    log_file = os.getenv("LOG_FILE_" + __package__.upper(), None)

    my_logger = logging.getLogger(__package__)
    my_logger.setLevel(log_level)

    if log_file is None:
        handler = logging.StreamHandler()
    else:
        handler = logging.FileHandler(log_file)

    formatter = logging.Formatter(log_format)
    formatter.datefmt = log_datefmt

    handler.setFormatter(formatter)
    my_logger.addHandler(handler)

    return my_logger


logger = create_logger()
# pylint: disable=missing-function-docstring
