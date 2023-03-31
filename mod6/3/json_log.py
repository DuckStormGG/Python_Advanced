import getpass
import hashlib
import json
import logging
import re
import string
from typing import Any, MutableMapping

logger = logging.getLogger("password_checker")
class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return  json.dumps(msg, ensure_ascii=False) , kwargs


def input_and_check_password():
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)
        pass

    return False


def is_strong_password(password: str):
    if re.search("[a-zA-Z]", password):
        return False
    else:
        return True


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="stderr.txt", encoding="UTF-8",
                        format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}',
                        datefmt="%H:%M:%S")
    logger = JsonAdapter(logging.getLogger(__name__), extra=None)
    logger.info("Вы пытаетесь аутентифицироваться в SkillBox")
    logger.info('"')
    count_numbers = 3
    logger.info(f"У вас есть {count_numbers} попыток")
    while count_numbers > 0:
        if input_and_check_password():
            exit(0)
        count_numbers -= 1
    logger.error("Пользователь трижды ввёл неправильный пароль!")
    exit(1)
