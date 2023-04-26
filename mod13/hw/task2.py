"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""
import sqlite3
import csv


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file) as wrong_fees:
        for wrong_fee in csv.reader(wrong_fees):
            c.execute("""DELETE from table_fees
                        where truck_number = ? and timestamp = ?
                        """,(wrong_fee[0],wrong_fee[1]))


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")
