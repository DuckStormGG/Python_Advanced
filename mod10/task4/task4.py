import sqlite3

if __name__ == '__main__':
    with sqlite3.connect("hw_4_database.db") as db:
        cursor = db.cursor()
        print("Выяснить, сколько человек с острова N находятся за чертой бедности, то есть получает меньше 5000 гульденов в год.")
        cursor.execute("SELECT COUNT(salary) FROM salaries WHERE salary < 5000")
        print(cursor.fetchall()[0][0])
        print("Посчитать среднюю зарплату по острову N.")
        cursor.execute("SELECT AVG(salary) from salaries")
        print(cursor.fetchall()[0][0])
        print("Посчитать медианную зарплату по острову. ")
        cursor.execute("SELECT AVG(salary) FROM (SELECT salary FROM salaries ORDER BY salary LIMIT 2 - (SELECT COUNT(*) FROM salaries) % 2 OFFSET (SELECT (COUNT(*) - 1) / 2 FROM salaries))")
        print(cursor.fetchall()[0][0])
        print("Посчитать число социального неравенства F")
        cursor.execute("""SELECT 100 * ROUND(TOP10 / CAST(DOWN90 AS real), 2) FROM (
                    (
                        SELECT SUM(salary) as TOP10 FROM (
                        SELECT salary
                        FROM salaries
                        ORDER BY salary DESC
                        LIMIT 0.1 * (SELECT COUNT(salary) FROM salaries)
                    ))
                    JOIN
                    (
                        SELECT SUM(salary) as DOWN90 FROM (
                        SELECT salary
                        FROM salaries
                        ORDER BY salary
                        LIMIT 0.9 * (SELECT COUNT(salary) FROM salaries))))""")
        print(cursor.fetchall()[0][0])