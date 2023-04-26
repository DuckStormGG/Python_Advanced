"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3


ivan_sovin_salary = 100000

def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:
    c.execute("SELECT salary from table_effective_manager WHERE name = ? and name !='Иван Совин'",(name,))
    salary = c.fetchone()[0]
    if 1.1 * salary > ivan_sovin_salary:
        c.execute("DELETE from table_effective_manager WHERE name = ? and name != 'Иван Совин'",(name,))
    else:
        c.execute("""
        UPDATE table_effective_manager
        SET salary = round(1.1 * salary)
        WHERE name = ?
          AND name != 'Иван Совин'
        """,(name,))


if __name__ == '__main__':
    name = input("Введите имя: ")
    with sqlite3.connect("hw.db") as db:
        c = db.cursor()
        ivan_sovin_the_most_effective(c, name)
