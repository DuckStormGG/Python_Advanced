import sys

from flask import Flask
from datetime import datetime

app = Flask(__name__)
weekday_num = datetime.today().weekday()
weekdays =("Понедельника","Вторника","Среды","Четверга","Пятницы","Субботы","Воскресенья")


@app.route( "/hello-world/<name>")
def hello_world_name(name):
    phrase = f"Привет, {name}."
    if weekday_num in (0,1,3,6):
        phrase += f" Хорошего {weekdays[weekday_num]}!"
    else:
        phrase += f" Хорошей {weekdays[weekday_num]}!"
    return phrase


if __name__ == "__main__":
    app.run(debug=True)
