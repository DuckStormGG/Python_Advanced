"""
На заводе "Дружба" работает очень дружный коллектив.
Рабочие работают посменно, в смене -- 10 человек.
На смену заходит 366 .

Бухгалтер завода составила расписание смен и занесла его в базу данных
    в таблицу `table_work_schedule`, но совершенно не учла тот факт,
    что все сотрудники люди спортивные и ходят на различные спортивные кружки:
        1. футбол (проходит по понедельникам)
        2. хоккей (по вторникам
        3. шахматы (среды)
        4. SUP сёрфинг (четверг)
        5. бокс (пятница)
        6. Dota2 (суббота)
        7. шах-бокс (воскресенье)

Как вы видите, тренировки по этим видам спорта проходят в определённый день недели.

Пожалуйста помогите изменить расписание смен с учётом личных предпочтений коллектива
    (или докажите, что то, чего они хотят - не возможно).
"""
import random
import sqlite3
import datetime

class Worker:
    def __init__(self,id,sport_day):
        self.id = id
        self.sport_day = sport_day
    def can_work(self,week_day):
        return self.sport_day != week_day.weekday()


sport_types ={
    "футбол":0,
    "хоккей":1,
    "шахматы":2,
    "SUP сёрфинг":3,
    "бокс":4,
    "Dota2":5,
    "шах-бокс":6
}

def update_work_schedule(c: sqlite3.Cursor) -> None:
    c.execute("DELETE FROM table_friendship_schedule")
    workers = []
    c.execute("SELECT id, preferable_sport from table_friendship_employees")
    raw_data = c.fetchall()
    for i in raw_data:
        workers.append(Worker(i[0],sport_types[i[1]]))
    first_day = datetime.date(year=2020,month=1,day=1)
    for i in range(0,366):
        day = first_day + datetime.timedelta(days=i)
        for j in range (10):
            worker_not_inserted = True
            while  worker_not_inserted:
                worker = random.choice(workers)
                if worker.can_work(day):
                    c.execute("INSERT INTO table_friendship_schedule(employee_id, date) VALUES (?,?)",(worker.id,day))
                    worker_not_inserted = False


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as db:
        c = db.cursor()
        update_work_schedule(c)



