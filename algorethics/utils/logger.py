import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name='algorethics_logger', log_file='algorethics.log', level=logging.INFO):
    """
    Setup a logger for the Algorethics AI library.

    Parameters:
    - name (str): The name of the logger.
    - log_file (str): File to which logs will be written.
    - level (logging.Level): The threshold for logging messages.

    Returns:
    - logging.Logger: A configured logger instance.
    """
    # Create a logger object
    logger = logging.getLogger(name)
    logger.setLevel(level)  # Set the logging level

    # Create file handler which logs even debug messages
    fh = RotatingFileHandler(log_file, maxBytes=10000, backupCount=5)
    fh.setLevel(level)

    # Create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)  # Only log errors and above to the console

    # Create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

# Example of setting up and using the logger
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger initialized')
    logger.debug('This is a debug message')
    logger.error('This is an error message')
