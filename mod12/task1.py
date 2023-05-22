import ast
import random
import time
from multiprocessing import Pool, cpu_count
from multiprocessing.pool import ThreadPool

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


def get_people(val) -> tuple:
    json = requests.get(URL.format(val))
    data = ast.literal_eval(json.content.decode())
    return data['name'], data['gender']

def gen_random_list(len):
    l = []
    for _ in range(len):
        i = 17
        while i == 17 or i in l:
            i = random.randrange(1,83)
        l.append(i)
    return l





def load_char_pool(c:sqlite3.Cursor):
    random_list = gen_random_list(20)
    pool = Pool(processes=cpu_count())
    start = time.perf_counter()
    all_chars = pool.map(get_people, random_list)
    pool.close()
    pool.join()
    for char in all_chars:
        c.execute("""INSERT INTO Characters(character_first_name, character_gender)
                                                    VALUES (?, ?)""", char)

    print(f'time: {time.perf_counter() - start}')

def load_people_thread_pool(c:sqlite3.Cursor):
    random_list = gen_random_list(20)
    pool = ThreadPool(processes=cpu_count())
    start = time.perf_counter()
    all_chars = pool.map(get_people, random_list)
    pool.close()
    pool.join()
    for char in all_chars:
        c.execute("""INSERT INTO Characters(character_first_name, character_gender)
                                                        VALUES (?, ?)""", char)

    print(f'threads time: {time.perf_counter() - start}')


def main():
    with sqlite3.connect('Characters.sqlite',check_same_thread=False) as db:
        c = db.cursor()
        c.execute("DROP TABLE IF EXISTS 'characters';")
        c.execute(CREATE_DATABASE_QUERY)
        load_char_pool(c)
        load_people_thread_pool(c)
#
if __name__ == '__main__':
    main()
