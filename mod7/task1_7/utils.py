import logging
import logging.handlers

logger = logging.getLogger("app_logger.utils_logger")
logger.debug("ÎŒØ∏‡°⁄·°€йцукен")

def addition(a, b) -> int:
    logger.info(f'{a} + {b} = {a+b}')
    return a + b


def subtraction(a, b) -> int:
    logger.info(f'{a} - {b} = {a - b}')
    return a - b


def multiplication(a, b) -> int:
    logger.info(f'{a} * {b} = {a * b}')
    return a * b


def division(a, b) -> float:
    logger.info(f'{a} / {b} = {a / b}')
    return a / b
