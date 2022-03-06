import configparser
import logging
from sys import stdout


class Helper:
    __config = None
    __logger = None

    def get_config():
        if Helper.__config is None:
            Helper.__config = configparser.ConfigParser()
            Helper.__config.read('./configurations.ini')
        return Helper.__config

    def get_log():
        if Helper.__logger is None:
            Helper.__logger = logging.getLogger('MT')
            log_level = Helper.get_config()['General']['LogLevel']
            Helper.__logger.setLevel(logging.getLevelName(log_level))
            if log_level == 'DEBUG':
                logFormatter = logging.Formatter(
                    "%(name)s %(asctime)s %(levelname)-4s %(filename)s:%(funcName)s | %(message)s", "%Y-%m-%d %H:%M:%S")
            else:
                logFormatter = logging.Formatter(
                    "%(name)s %(asctime)s %(levelname)-4s | %(message)s", "%Y-%m-%d %H:%M:%S")
            consoleHandler = logging.StreamHandler(stdout)
            consoleHandler.setFormatter(logFormatter)
            Helper.__logger.addHandler(consoleHandler)
        return Helper.__logger

    def progress(count, total, suffix=''):
        bar_len = 42
        filled_len = int(round(bar_len * count / float(total)))
        percents = round(100.0 * count / float(total), 0)
        bar = '■' * filled_len + '-' * (bar_len - filled_len)
        Helper.get_log().info('[%s] %3.0f (%s %s)\r' % (bar, percents, '%', suffix))
        # sys.stdout.flush()