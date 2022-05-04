from psycopg2.extras import execute_batch


PAGE_SIZE = 10


class PostgresSaver:
    def __init__(self, pg_conn):
        self.cur = pg_conn.cursor()

    def save_all_data(self, data):
        try:
            query_insert_filmworks = '''insert into content.film_work
            (id,
            title,
            description,
            creation_date,
            rating,
            type,
            created,
            modified)
            values (%s, %s, %s, %s, %s, %s, %s, %s)
            on conflict (id) do nothing;'''
            data_film_work = [(
                filmwork.id,
                filmwork.title,
                filmwork.description,
                filmwork.creation_date,
                filmwork.rating,
                filmwork.type,
                filmwork.created_at,
                filmwork.updated_at
                )
                for filmwork in data['filmworks']]
            execute_batch(
                self.cur,
                query_insert_filmworks,
                data_film_work,
                page_size=PAGE_SIZE)
        except Exception as e:
            print("Загрузка в postgres таблица content.film_work")
            print(e)

        try:
            query_insert_persons = '''insert into content.person
            (id, full_name, created, modified)
            values (%s, %s, %s, %s)
            on conflict (id) do nothing;
            '''
            data_person = [(
                person.id,
                person.full_name,
                person.created_at,
                person.updated_at
                )
                for person in data['persons']]
            execute_batch(
                self.cur,
                query_insert_persons,
                data_person,
                page_size=PAGE_SIZE)
        except Exception as e:
            print("Загрузка в postgres таблица content.person")
            print(e)

        try:
            query_insert_genres = '''insert into content.genre
            (id, name, description, created, modified)
            values (%s, %s, %s, %s, %s)
            on conflict (id) do nothing;
            '''
            data_genre = [(
                genre.id,
                genre.name,
                genre.description,
                genre.created_at,
                genre.updated_at
                )
                for genre in data['genres']]
            execute_batch(
                self.cur,
                query_insert_genres,
                data_genre,
                page_size=PAGE_SIZE)
        except Exception as e:
            print("Загрузка в postgres таблица content.genre")
            print(e)

        try:
            query_insert_person_filmworks = '''insert into content.person_film_work
            (id, film_work_id, person_id, role, created)
            values (%s, %s, %s, %s, %s)
            on conflict (id) do nothing;
            '''
            data_person_filmworks = [(
                person_filmwork.id,
                person_filmwork.film_work_id,
                person_filmwork.person_id,
                person_filmwork.role,
                person_filmwork.created_at
                )
                for person_filmwork in data['person_filmworks']]
            execute_batch(
                self.cur,
                query_insert_person_filmworks,
                data_person_filmworks,
                page_size=PAGE_SIZE)
        except Exception as e:
            print("Загрузка в postgres таблица content.person_film_work")
            print(e)

        try:
            query_insert_genre_filmworks = '''insert into content.genre_film_work
            (id, genre_id, film_work_id, created)
            values (%s, %s, %s, %s)
            on conflict (id) do nothing;
            '''
            data_genre_filmworks = [(
                genre_filmwork.id,
                genre_filmwork.genre_id,
                genre_filmwork.film_work_id,
                genre_filmwork.created_at
                )
                for genre_filmwork in data['genre_filmworks']]
            execute_batch(
                self.cur,
                query_insert_genre_filmworks,
                data_genre_filmworks,
                page_size=PAGE_SIZE)
        except Exception as e:
            print("Загрузка в postgres таблица content.genre_film_work")
            print(e)

        self.cur.close()
