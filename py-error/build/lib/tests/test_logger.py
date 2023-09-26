# tests/test_logger.py

import unittest
from toolkit.logger import setup_logger
import logging
import os

class TestLogger(unittest.TestCase):

    def test_setup_logger(self):
        log_file = 'test.log'

        # Ensure the log file does not exist initially
        if os.path.exists(log_file):
            os.remove(log_file)

        logger = setup_logger(log_file)

        # Check if the logger is an instance of logging.Logger
        self.assertIsInstance(logger, logging.Logger)

        # Log some messages
        logger.info("This is an info message.")
        logger.warning("This is a warning message.")
        logger.error("This is an error message.")

        # Ensure the log file exists after logging
        self.assertTrue(os.path.exists(log_file))

        # Clean up: remove the log file
        os.remove(log_file)

if __name__ == '__main__':
    unittest.main()