import sqlite3
import psycopg2
import os
import logging
from psycopg2.extensions import connection as _connection
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

from sqlite_loader import SQLiteLoader
from postgres_saver import PostgresSaver


def load_from_sqlite(connection: sqlite3.Connection, pg_conn: _connection):
    """Основной метод загрузки данных из SQLite в Postgres"""
    postgres_saver = PostgresSaver(pg_conn)
    sqlite_loader = SQLiteLoader(connection)
    tables = [
        'film_work',
        'person',
        'genre',
        'person_film_work',
        'genre_film_work']
    for table in tables:
        sqlite_loader.cursor.execute('select * from {}'.format(table))
        gen_load = sqlite_loader.load_data(table)
        for data in gen_load:
            postgres_saver.save_all_data(data)

    sqlite_loader.cursor.close()
    postgres_saver.cur.close()


if __name__ == '__main__':
    load_dotenv()
    logging.basicConfig(filename='load_data.log',
                        filemode='a',
                        level=logging.INFO)
    dsl = {'dbname': os.environ.get('DB_NAME'),
           'user': os.environ.get('DB_USER'),
           'password': os.environ.get('DB_PASSWORD'),
           'host': os.environ.get('DB_HOST', '127.0.0.1'),
           'port': os.environ.get('DB_PORT', 5432)}
    with sqlite3.connect('03_sqlite_to_postgres/db.sqlite') as sqlite_conn,\
            psycopg2.connect(**dsl, cursor_factory=DictCursor) as pg_conn:
        load_from_sqlite(sqlite_conn, pg_conn)
