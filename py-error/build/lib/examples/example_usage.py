# examples/example_usage.py

from toolkit.error_handler import CustomError, handle_error
from toolkit.logger import setup_logger

def main():
    # Initialize the logger
    logger = setup_logger('example.log')

    try:
        # Simulate an error
        simulate_error()
    except Exception as e:
        handle_error(e, log_function=logger.error)

def simulate_error():
    # Simulate a custom error
    try:
        # Code that may raise exceptions
        raise CustomError("This is a custom error.")
    except CustomError as ce:
        handle_error(ce)
    except Exception as e:
        handle_error(e)

if __name__ == "__main__":
    main()