import sqlite3


if __name__ == '__main__':
    with sqlite3.connect("hw_3_database.db") as db:
        cursor = db.cursor()
        print("Сколько записей (строк) хранится в каждой таблице?")
        cursor.execute("SELECT COUNT(*) FROM table_1")
        print(f"table_1 = {cursor.fetchall()[0][0]}")
        cursor.execute("SELECT COUNT(*) FROM table_2")
        print(f"table_2 = {cursor.fetchall()[0][0]}")
        cursor.execute("SELECT COUNT(*) FROM table_3")
        print(f"table_3 = {cursor.fetchall()[0][0]}")
        print("Сколько в таблице table_1 уникальных записей?")
        cursor.execute("SELECT COUNT(DISTINCT value) from table_1")
        print(f"table_1 = {cursor.fetchall()[0][0]}")
        print("Как много записей из таблицы table_1 встречается в table_2?")
        cursor.execute("SELECT COUNT(DISTINCT (table_1.value)) FROM table_1 INNER JOIN table_2 t2 on table_1.value = t2.value")
        print(cursor.fetchall()[0][0])
        print("Как много записей из таблицы table_1 встречается и в table_2, и в table_3?")
        cursor.execute("SELECT COUNT(DISTINCT (table_1.value)) FROM table_1 INNER JOIN table_2 t2 on table_1.value = t2.value INNER JOIN table_3 t3 on table_1.value = t3.value")
        print(cursor.fetchall()[0][0])
