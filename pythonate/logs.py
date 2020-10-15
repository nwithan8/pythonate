import logging

# Logging #
need_to_config_logs = True


def _info(message):
    logging.info(msg=message)


def _error(message):
    logging.error(msg=message)


def _warning(message):
    logging.warning(msg=message)


level_map = {
    'info': _info,
    'error': _error,
    'warning': _warning
}


def log(message: str, level: str = "info") -> None:
    """
    Log a message if verbose is enabled.
    :param message: Message to log
    :param level: info, error or warning
    """
    if need_to_config_logs:
        init_logging()
    if level not in level_map.keys():
        level = 'info'
    level_map[level](message)


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
