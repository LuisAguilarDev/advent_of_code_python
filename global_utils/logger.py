import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ColorFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: "\x1b[36m",    # cyan
        logging.INFO: "\x1b[32m",     # green
        logging.WARNING: "\x1b[33m",  # yellow
        logging.ERROR: "\x1b[31m",    # red
        logging.CRITICAL: "\x1b[41m\x1b[37m",  # white on red
    }
    RESET = "\x1b[0m"

    def __init__(self, fmt=None, datefmt=None):
        super().__init__(fmt or "%(levelname)s: %(message)s", datefmt)

    def format(self, record):
        text = super().format(record)
        color = self.COLORS.get(record.levelno, "")
        return f"{color}{text}{self.RESET}" if color else text


  # Add a single StreamHandler (avoid duplicate handlers on reload)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(ColorFormatter())
    logger.addHandler(handler)
