# ================================================================================================= #
""" Description: Contains the implementation of a Logger for the LRU Cache """
# ================================================================================================= #
__author__ = "Shrey Tiwari"
__copyright__ = "Copyright 2021, LRU Cache"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Shrey Tiwari"
__email__ = "shreymt@gmail.com"
__status__ = 'Prototype'
# ================================================================================================= #

# Importing the required modules
import logging


class logger_wrapper:
    def __init__(self, name='LRU Cache', level=logging.DEBUG, file='Logs.log'):
        self.name = name
        self.level = level
        self.file = file
        self.formatter = logging.Formatter('| %(asctime)s | %(name)s | %(levelname)s\t| %(funcName)s\t| %(message)s')

    def new_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)
        handler = logging.FileHandler(self.file)
        handler.setFormatter(self.formatter)
        logger.addHandler(handler)

        return logger


# Function to manually test functionality
def test():
    log_wrapper = logger_wrapper()
    logger = log_wrapper.new_logger()
    logger.debug("Hello world!")
    logger.info("This is a test message")
    logger.warning("Being printed from the logger wrapper class")
    logger.error("To ensure appropriate formatting of logs")
    logger.critical("And the correctness of code.")


if __name__ == '__main__':
    test()
