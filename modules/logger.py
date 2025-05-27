import logging
import os

def get_logger(name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Console Handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # File Handler
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add Handlers
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger