import sqlite3

from classes import Filmwork, Person, Genre, PersonFilmwork, GenreFilmWork


class SQLiteLoader:
    def __init__(self, sqlite_conn):
        sqlite_conn.row_factory = sqlite3.Row
        self.cursor = sqlite_conn.cursor()

    def load_movies(self):
        try:
            self.cursor.execute("select * from film_work;")
            data_filmworks = self.cursor.fetchall()
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
        except Exception as e:
            print("Загрузка из sqlite таблица film_work")
            print(e)

        try:
            self.cursor.execute("select * from person;")
            data_persons = self.cursor.fetchall()
            persons = [Person(
                full_name=person['full_name'],
                id=person['id'],
                created_at=person['created_at'],
                updated_at=person['updated_at'])
                for person in data_persons]
        except Exception as e:
            print("Загрузка из person")
            print(e)

        try:
            self.cursor.execute("select * from genre;")
            data_genre = self.cursor.fetchall()
            genres = [Genre(
                name=genre['name'],
                description=genre['description'],
                id=genre['id'],
                created_at=genre['created_at'],
                updated_at=genre['updated_at'])
                for genre in data_genre]
        except Exception as e:
            print("Загрузка из sqlite таблица genre")
            print(e)

        try:
            self.cursor.execute("select * from person_film_work;")
            person_filmwork_data = self.cursor.fetchall()
            person_filmworks = [PersonFilmwork(
                film_work_id=person_filmwork['film_work_id'],
                person_id=person_filmwork['person_id'],
                role=person_filmwork['role'],
                id=person_filmwork['id'],
                created_at=person_filmwork['created_at']
            ) for person_filmwork in person_filmwork_data]
        except Exception as e:
            print("Загрузка из sqlite таблица person_film_work")
            print(e)

        try:
            self.cursor.execute("select * from genre_film_work;")
            genre_filmwork_data = self.cursor.fetchall()
            genre_filmworks = [GenreFilmWork(
                genre_id=genre_filmwork['genre_id'],
                film_work_id=genre_filmwork['film_work_id'],
                id=genre_filmwork['id'],
                created_at=genre_filmwork['created_at']
            ) for genre_filmwork in genre_filmwork_data]
        except Exception as e:
            print("Загрузка из sqlite таблица genre_film_work")
            print(e)

        self.cursor.close()
        data = {
            'filmworks': filmworks,
            'persons': persons,
            'genres': genres,
            'person_filmworks': person_filmworks,
            'genre_filmworks': genre_filmworks
        }
        return data
