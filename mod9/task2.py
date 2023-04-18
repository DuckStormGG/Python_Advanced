from flask import Flask
from datetime import datetime

APP = Flask(__name__)
HOST = '0.0.0.0'
PORT = 5000
SERVICE_NAME = 'application'


WEEKDAYS =("Понедельника", "Вторника", "Среды", "Четверга", "Пятницы", "Субботы", "Воскресенья")


@APP.route( "/hello-world/<name>")
def hello_world_name(name):
    weekday_num = datetime.today().weekday()
    phrase = f"Привет, {name} от {SERVICE_NAME}.\n"
    if weekday_num in (0,1,3,6):
        phrase += f" Хорошего {WEEKDAYS[weekday_num]}!"
    else:
        phrase += f" Хорошей {WEEKDAYS[weekday_num]}!"
    return phrase


if __name__ == "__main__":
    APP.run(host=HOST, port=PORT)
