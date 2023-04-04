import logging
import logging.config
import logging_tree


from sys import stdout
from logging_config import dict_config
from mod7.task1_7 import utils
from logging import Filter

from mod7.task1_7.LogToFIleHandler import LogToFileHandler

logging.config.dictConfig(dict_config)

logger = logging.getLogger("app_logger")

# custom_handler = logging.StreamHandler(stream=stdout)
# formatter =  logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s,| %(lineno)s | %(message)s", datefmt="%H:%M:%S")
# custom_handler.setFormatter(formatter)
# new_handler = LogToFileHandler()
# new_handler.setFormatter(formatter)

# logging.basicConfig(level='DEBUG', handlers=[custom_handler, new_handler])

ascii_filter = Filter("app_logger")

with open("logging_tree.txt", "w") as file:
    file.write(logging_tree.format.build_description())

# logger.info("TEST")
# logger.error("TEST")
# logger.warning("TEST")
# logger.critical("TEST")
#
# logger.debug("ÎŒØ∏‡°⁄·°€йцукен")


while True:
    command = input().split()
    try:
        if command[1] == "+":
            logger.debug("addition ")
            print(utils.addition(int(command[0]), int(command[2])))
        elif command[1] == '-':
            logger.debug("subtraction ")
            print(utils.subtraction(int(command[0]), int(command[2])))
        elif command[1] == '*':
            logger.debug("multiplication ")
            print(utils.multiplication(int(command[0]), int(command[2])))
        elif command[1] == '/':
            logger.debug("division ")
            print(utils.division(int(command[0]), int(command[2])))
        else:
            raise Exception(f"wrong command: {' '.join(command)}")
    except Exception as e:
        logger.error(f"{e}")

