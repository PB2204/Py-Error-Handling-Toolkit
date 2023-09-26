# toolkit/error_handler.py

class CustomError(Exception):
    """
    A custom exception class for handling specific types of errors.
    You can create instances of this class with a custom error message.
    """
    def __init__(self, message):
        super().__init__(message)

def handle_error(error, log_function=None):
    """
    Handle errors based on their type.

    :param error: The error to handle.
    :param log_function: An optional logging function (e.g., logger.error) to log the error.
    """
    if isinstance(error, CustomError):
        error_message = f"Custom error occurred: {error}"
        # Add custom error handling logic here
        if log_function:
            log_function(error_message)
        else:
            print(error_message)
    else:
        error_message = f"An unexpected error occurred: {error}"
        # Add generic error handling logic here
        if log_function:
            log_function(error_message)
        else:
            print(error_message)

if __name__ == "__main__":
    # Example usage
    try:
        # Code that may raise exceptions
        raise CustomError("This is a custom error.")
    except CustomError as ce:
        handle_error(ce)
    except Exception as e:
        handle_error(e)
    else:
        print("No errors occurred.")