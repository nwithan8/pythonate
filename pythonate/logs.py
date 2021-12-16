import logging

# Logging #
from enum import Enum

need_to_config_logs = True


def _critical(message):
    logging.critical(msg=message)


def _info(message):
    logging.info(msg=message)


def _error(message):
    logging.error(msg=message)


def _warning(message):
    logging.warning(msg=message)


def _debug(message):
    logging.debug(msg=message)


class LogLevel(Enum):
    CRITICAL = _critical
    FATAL = _critical
    ERROR = _error
    WARNING = _warning
    INFO = _info
    DEBUG = _debug


def log(message: str, level: LogLevel = LogLevel.INFO) -> None:
    """
    Log a message if verbose is enabled.
    :param message: Message to log
    :param level: debug, info, warning, error or critical
    """
    if need_to_config_logs:
        init_logging()
    level.value(message)


def init_logging(message_format: str = '%(asctime)s %(levelname)s:%(message)s',
                 verbose: bool = False,
                 re_init: bool = False):
    """
    Initialize logging.
    :param message_format: Format of log entries
    :param verbose: Should INFO statements be logged? (Default: False)
    :param re_init: Reconfigure logging with new message_format and verbose settings (Default: False)
    """
    global need_to_config_logs
    if need_to_config_logs or re_init:
        logging.basicConfig(format=message_format,
                            level=(logging.INFO if verbose else logging.ERROR))
        need_to_config_logs = False
