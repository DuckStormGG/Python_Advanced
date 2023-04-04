from mod7.task1_7.LogToFIleHandler import LogToFileHandler
from CustomFilter import AsciiFilter


dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format":"%(levelname)s | %(name)s | %(asctime)s,| %(lineno)s | %(message)s"}
    },
    "handlers": {
        "console_handler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filters": ["ascii_filer"]
        },
        "file_handler": {
            "()": LogToFileHandler,
            "level": "DEBUG",
            "formatter": "base",
            "filters": ["ascii_filer"]
        },
        "rotating_handler": {
            "class":"logging.handlers.TimedRotatingFileHandler",
            "when": "H",
            "interval": 10,
            "backupCount": 1,
            "level":"INFO",
            "formatter": "base",
            "filename": "utils.log",
            "filters": ["ascii_filer"]
        },
        "http_handler":{
            "class":"logging.handlers.HTTPHandler",
            "host": "127.0.0.1:5000",
            "url": "logs",
            "method": "POST"
        }
    },
    "loggers": {
        "app_logger":{
            "level": "DEBUG",
            "handlers": ["console_handler","file_handler","http_handler"]
        },
        "app_logger.utils_logger":{
            "level": "DEBUG",
            "handlers": ["console_handler", "file_handler", "rotating_handler", "http_handler"],
            "propagate": False
        }
    },
    "filters": {
        "ascii_filer": {
            "()": AsciiFilter
        }
    }
}