# tests/test_error_handler.py

from toolkit.error_handler import CustomError, handle_error
import unittest
from unittest.mock import patch
from io import StringIO

class TestErrorHandler(unittest.TestCase):

    def setUp(self):
        self.error_stream = StringIO()
        self.error_logger = CustomError("Test error message")
        self.generic_exception = Exception("Test generic exception")

    def test_custom_error_message(self):
        with patch('sys.stderr', self.error_stream):
            handle_error(self.error_logger)
        self.assertEqual(
            self.error_stream.getvalue().strip(),
            "Custom error occurred: Test error message"
        )

    def test_generic_error_message(self):
        with patch('sys.stderr', self.error_stream):
            handle_error(self.generic_exception)
        self.assertEqual(
            self.error_stream.getvalue().strip(),
            "An unexpected error occurred: Test generic exception"
        )

if __name__ == '__main__':
    unittest.main()