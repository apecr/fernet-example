import logging, logging.config

import yaml


def _get_logger_configuration_function():
    logger = None

    def _configure_logger():
        nonlocal logger

        if logger is None:
            logging.config.dictConfig(yaml.safe_load(open("logging.conf")))
            logger = logging.getLogger()

        return logger

    return _configure_logger


configure_logger = _get_logger_configuration_function()
