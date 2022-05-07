import sqlite3
import logging
from classes import Filmwork, Person, Genre, PersonFilmwork, GenreFilmWork


class SQLiteLoader:
    def __init__(self, sqlite_conn):
        sqlite_conn.row_factory = sqlite3.Row
        self.cursor = sqlite_conn.cursor()
        self.SIZE = 500

    def load_filmworks(self):
        while True:
            try:
                data_filmworks = self.cursor.fetchmany(self.SIZE)
                if not data_filmworks:
                    break
                filmworks = [Filmwork(
                    title=filmwork['title'],
                    description=filmwork['description'],
                    file_path=filmwork['file_path'],
                    creation_date=filmwork['creation_date'],
                    type=filmwork['type'],
                    id=filmwork['id'],
                    rating=filmwork['rating'],
                    created_at=filmwork['created_at'],
                    updated_at=filmwork['updated_at'])
                    for filmwork in data_filmworks]
                yield {'filmworks': filmworks}
            except Exception as e:
                logging.info("Загрузка из sqlite таблица film_work")
                logging.exception(e)
                break

    def load_persons(self):
        while True:
            try:
                data_persons = self.cursor.fetchmany(self.SIZE)
                if not data_persons:
                    break
                persons = [Person(
                    full_name=person['full_name'],
                    id=person['id'],
                    created_at=person['created_at'],
                    updated_at=person['updated_at'])
                    for person in data_persons]
                yield {'persons': persons}
            except Exception as e:
                logging.info("Загрузка из person")
                logging.exception(e)
                break

    def load_genres(self):
        while True:
            try:
                data_genre = self.cursor.fetchmany(self.SIZE)
                if not data_genre:
                    break
                genres = [Genre(
                    name=genre['name'],
                    description=genre['description'],
                    id=genre['id'],
                    created_at=genre['created_at'],
                    updated_at=genre['updated_at'])
                    for genre in data_genre]
                yield {'genres': genres}
            except Exception as e:
                logging.info("Загрузка из sqlite таблица genre")
                logging.exception(e)
                break

    def load_person_filmworks(self):
        while True:
            try:
                person_filmwork_data = self.cursor.fetchmany(self.SIZE)
                if not person_filmwork_data:
                    break
                person_filmworks = [PersonFilmwork(
                    film_work_id=person_filmwork['film_work_id'],
                    person_id=person_filmwork['person_id'],
                    role=person_filmwork['role'],
                    id=person_filmwork['id'],
                    created_at=person_filmwork['created_at']
                ) for person_filmwork in person_filmwork_data]
                yield {'person_filmworks': person_filmworks}
            except Exception as e:
                logging.info("Загрузка из sqlite таблица person_film_work")
                logging.exception(e)
                break

    def load_genre_filmworks(self):
        while True:
            try:
                genre_filmwork_data = self.cursor.fetchmany(self.SIZE)
                if not genre_filmwork_data:
                    break
                genre_filmworks = [GenreFilmWork(
                    genre_id=genre_filmwork['genre_id'],
                    film_work_id=genre_filmwork['film_work_id'],
                    id=genre_filmwork['id'],
                    created_at=genre_filmwork['created_at']
                ) for genre_filmwork in genre_filmwork_data]
                yield {'genre_filmworks': genre_filmworks}
            except Exception as e:
                logging.info("Загрузка из sqlite таблица genre_film_work")
                logging.exception(e)
                break

    def load_data(self, table):
        load = {
            'film_work': self.load_filmworks,
            'person': self.load_persons,
            'genre': self.load_genres,
            'person_film_work': self.load_person_filmworks,
            'genre_film_work': self.load_genre_filmworks
        }

        return load[table]()
