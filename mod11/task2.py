import ast
import random
import time

import requests
import sqlite3
import threading

URL = "https://swapi.dev/api/people/{}"

CREATE_DATABASE_QUERY = """
CREATE TABLE 'characters'(
    character_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    character_first_name VARCHAR(50) NOT NULL,
    character_gender VARCHAR(20) NOT NULL
);
"""
lock = threading.Lock()

def get_people(c:sqlite3.Cursor):
    json = requests.get(URL.format(random.randrange(1,83)))
    data = ast.literal_eval(json.content.decode())
    with lock:
        c.execute("""INSERT INTO Characters(character_first_name, character_gender)
                                            VALUES (?, ?)""", (data['name'], data['gender'],))




def load_char_seq(c:sqlite3.Cursor):
    start = time.perf_counter()
    for _ in range(20):
        get_people(c)
    print(f'time: {time.perf_counter() - start}')

def load_people_threads(c:sqlite3.Cursor):
    start = time.perf_counter()
    threads = []
    for _ in range(20):
        thread = threading.Thread(target=get_people, args=(c,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(f'threads time: {time.perf_counter() - start}')


def main():
    with sqlite3.connect('Characters.sqlite',check_same_thread=False) as db:
        c = db.cursor()
        c.execute("DROP TABLE IF EXISTS 'characters';")
        c.execute(CREATE_DATABASE_QUERY)
        load_char_seq(c)
        load_people_threads(c)

if __name__ == '__main__':
    main()