"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3
import random

countries = ['Германия','Франция','Россия','Португалия','Бельгия','Италия','Швейцария','Польша']
strength = ['Сильная', 'Слабая','Средняя','Средняя']

def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    j = 0
    group = 1
    c.execute("DELETE FROM uefa_commands")
    c.execute("DELETE FROM uefa_draw")
    for i in range(number_of_groups * 4):
        country = random.choice(countries)
        c.execute("""INSERT INTO uefa_commands(command_number, command_name, command_country, command_level)
                                VALUES (?, ?, ?, ?)""",(i+1,f"{strength[j]}_{country}",country,strength[j]))
        c.execute("""INSERT INTO uefa_draw(command_number, group_number) VALUES (?,?)""",(i+1, group))
        j += 1
        if j == 4:
            group += 1
            j = 0






if __name__ == '__main__':
    with sqlite3.connect('hw.db') as db:
        c = db.cursor()
        generate_test_data(c,int(input("Введите кол-во групп: ")))