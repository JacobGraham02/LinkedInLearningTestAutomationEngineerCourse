import logging
# Creates logger with the name of the module
logger = logging.getLogger(__name__)
# By default, all loggers will propagate (share) its messages up to the Python default (base) logger. You can override this by specifying the propagate property as false
logger.propagate = False
logger.info('hello from helper')