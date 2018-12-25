import logging
import os

log_dir = os.getenv("log_dir")
log_filename = os.getenv("log_filename")
user_pass = os.getenv("user_pass")


def getLogger():

    logger = logging.getLogger("bigdata_services")

    # Replace the previous handlers with the new FileHandler
    for old_handler in logger.handlers:
        logger.removeHandler(old_handler)

    return logger


def getLoggingInstance():

    log_path=log_dir+log_filename

    bigdata_logging = getLogger()

    bigdata_logging.setLevel(logging.DEBUG)

    # create a log dir
    if not os.path.exists(log_dir):
        os.mkdir(log_dir)

    # create a file handler
    handler_file = logging.FileHandler(log_path, mode='a', encoding=None, delay=False)

    # create a logging format
    formatter = logging.Formatter(
        '{"time":"%(asctime)s", "level":"%(levelname)s","file":"%(filename)s","module":"%(module)s","function":"%(funcName)s","lineno":"%(lineno)d",'
        '"msg":"%(message)s"}')
    handler_file.setFormatter(formatter)

    # add the handlers to the logger
    bigdata_logging.addHandler(handler_file)

    return bigdata_logging