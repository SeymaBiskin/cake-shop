import logging


class LoggerFactory:

    _instance = None

    def __new__(cls, file_name="", log_level=logging.INFO, file_format="log"):
        if cls._instance is None:
            cls._instance = super(LoggerFactory, cls).__new__(cls)
            cls._instance.logger = cls._configure_logger(file_name, log_level, file_format)
        return cls._instance

    @staticmethod
    def _configure_logger(file_name, log_level, file_format):
        logger = logging.getLogger("logger")
        logger.setLevel(log_level)

        # Create a file handler and set the log level
        file_handler = logging.FileHandler(f"{file_name}.{file_format}")
        file_handler.setLevel(log_level)

        # Define the log format
        log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(log_format)

        # Add the handlers to the logger
        logger.addHandler(file_handler)

        return logger
