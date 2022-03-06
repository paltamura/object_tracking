import configparser
import logging
from sys import stdout


class Helper:
    __config = None
    __logger = None

    # Read config
    def get_config():
        if Helper.__config is None:
            Helper.__config = configparser.ConfigParser()
            Helper.__config.read('./configurations.ini')
        return Helper.__config

    # Write log
    def get_log():
        if Helper.__logger is None:
            Helper.__logger = logging.getLogger('MT')
            log_level = Helper.get_config()['General']['LogLevel']
            # Helper.__logger.setLevel(logging.DEBUG)  # set logger level
            Helper.__logger.setLevel(logging.getLevelName(log_level))  # set logger level

            if log_level == 'DEBUG':
                logFormatter = logging.Formatter(
                    "%(name)s %(asctime)s %(levelname)-4s %(filename)s:%(funcName)s | %(message)s", "%Y-%m-%d %H:%M:%S")
            else:
                logFormatter = logging.Formatter(
                    "%(name)s %(asctime)s %(levelname)-4s | %(message)s", "%Y-%m-%d %H:%M:%S")

            consoleHandler = logging.StreamHandler(
                stdout)  # set streamhandler to stdout
            consoleHandler.setFormatter(logFormatter)
            Helper.__logger.addHandler(consoleHandler)
        return Helper.__logger