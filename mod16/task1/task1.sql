DROP TABLE IF EXISTS 'actors';

CREATE TABLE 'actors'(
    act_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    act_first_name VARCHAR(50) NOT NULL,
    act_last_name VARCHAR(50) NOT NULL,
    act_gender VARCHAR(1) NOT NULL
);

DROP TABLE IF EXISTS 'movie';

CREATE TABLE 'movie'(
    mov_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mov_title VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS 'director';

CREATE TABLE 'director'(
    dir_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    dir_first_name VARCHAR(50) NOT NULL,
    dir_last_name VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS 'movie_cast';

CREATE TABLE 'movie_cast'(
    act_id INTEGER NOT NULL REFERENCES actors(act_id) ON DELETE SET NULL,
    mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE SET NULL,
    role VARCHAR(50) NOT NULL
);

DROP TABLE IF EXISTS 'oscar_awarded';

CREATE TABLE 'oscar_awarded'(
    award_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE SET NULL
);

DROP TABLE IF EXISTS 'movie_direction';

CREATE TABLE 'movie_direction'(
    dir_id INTEGER NOT NULL REFERENCES director(dir_id) ON DELETE SET NULL,
    mov_id INTEGER NOT NULL REFERENCES movie(mov_id) ON DELETE SET NULL
);