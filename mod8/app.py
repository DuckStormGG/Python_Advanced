import os
import random
import string

from flask import Flask, render_template, send_from_directory
from datetime import datetime, timedelta


car_list = ["Chevrolet", " Renault", " Ford", "Lada"]
cat_list = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, "war_and_peace.txt")
punctuation = string.punctuation + "–«»123456789"
root = os.path.dirname(os.path.abspath(__file__))
static = os.path.join(root, 'static')

app = Flask(__name__, static_folder=static, template_folder=root)


def get_word_list():
    book = []
    with open(BOOK_FILE, "r", encoding="UTF-8") as file:
        for line in file:
            temp = line.split()
            new_line = [word.translate(str.maketrans('', '', punctuation)) for word in temp]
            new_line = [s for s in new_line if s]
            book.extend(new_line)
    return book


@app.route("/hello_world")
def hello_world():
    return "Привет, мир!"


@app.route("/car")
def cars_list():
    return ", ".join(car_list)


@app.route("/cats")
def rnd_cat():
    return cat_list[random.randrange(0, len(cat_list) - 1)]


@app.route("/get_time/now")
def get_time_now():
    current_time = datetime.now()
    return f"Точное время: {current_time.time()}"


@app.route("/get_time/future")
def get_time_future():
    current_time_after_hour = datetime.now() + timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour.time()}"


@app.route("/get_random_word")
def get_random_word():
    word_list = get_word_list()
    return word_list[random.randrange(0, len(word_list) - 1)]


@app.route('/counter')
def counter():
    counter.visits += 1
    return str(counter.visits)

@app.route("/")
def snow():
    return render_template("index.html")

@app.route("/static/<path:path>")
def send_static(path):
    print(path)
    return send_from_directory(static, path)


counter.visits = 0

if __name__ == "__main__":
    app.run(debug=True)

