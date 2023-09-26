# toolkit/logger.py

import logging

def setup_logger(log_file):
    """
    Set up a basic logger and return it.

    :param log_file: The path to the log file.
    :return: The configured logger.
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define a log format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Create a file handler and set the formatter
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    # Example usage
    logger = setup_logger('error.log')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')
    logger.error('This is an error message.')