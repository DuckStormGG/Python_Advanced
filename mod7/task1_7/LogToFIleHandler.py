import logging

class LogToFileHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
    def emit(self, record: logging.LogRecord) -> None:
        message = self.format(record) + "\n"
        level = record.levelname
        if level == "DEBUG":
            with open("calc_debug.log", "a") as file :
                file.write(message)
        elif level == "INFO":
            with open("calc_info.log", "a") as file :
                file.write(message)
        elif level == "WARNING":
            with open("calc_warning.log", "a") as file :
                file.write(message)
        elif level == "ERROR":
            with open("calc_error.log", "a") as file :
                file.write(message)
        elif level == "CRITICAL":
            with open("calc_critical.log", "a") as file :
                file.write(message)
