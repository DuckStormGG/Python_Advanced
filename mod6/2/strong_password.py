import getpass
import hashlib
import logging
import re
import string

logger = logging.getLogger("password_checker")
words = []
def get_eng_words():
    with open("words.txt", "r") as file:
        for word in file:
            if len(word) > 4:
                words.append(word)


def is_strong_password(password: str):
    get_eng_words()
    for word in words:
        if password.lower() in word:
            return False
    return True


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




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="stderr.txt", encoding="UTF-8", format='%(asctime)s %(message)s',
                        datefmt="%H:%M:%S")
    logger.info("Вы пытаетесь аутентифицироваться в SkillBox")
    count_numbers = 3
    logger.info(f"У вас есть {count_numbers} попыток")
    while count_numbers > 0:
        if input_and_check_password():
            exit(0)
        count_numbers -= 1
    logger.error("Пользователь трижды ввёл неправильный пароль!")
    exit(1)
