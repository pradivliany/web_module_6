import sqlite3
import logging

DATABASE = "./homework.db"


def create_db_with_tables():
    """
    Функція створює БД (якщо до цього не існувала)
    та виконує SQL скрипт на створення таблиць
    :return: None
    """
    with open("SQL_scripts/create_tables.sql", "r") as file:
        sql = file.read()

    with sqlite3.connect(DATABASE) as connection:
        cursor = connection.cursor()
        try:
            cursor.executescript(sql)
            connection.commit()
        except sqlite3.Error as err:
            logging.error(err)


if __name__ == "__main__":
    create_db_with_tables()
