from dataclasses import dataclass, field
from datetime import date, datetime

import uuid


@dataclass
class Filmwork:
    title: str
    description: str
    file_path: str
    creation_date: date
    type: str

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    rating: float = field(default=0.0)
    created_at: datetime = field(default_factory=datetime.now())
    updated_at: datetime = field(default_factory=datetime.now())


@dataclass
class Person:
    full_name: str

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now())
    updated_at: datetime = field(default_factory=datetime.now())


@dataclass
class Genre:
    name: str
    description: str

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now())
    updated_at: datetime = field(default_factory=datetime.now())


@dataclass
class PersonFilmwork:
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now())


@dataclass
class GenreFilmWork:
    genre_id: uuid.UUID
    film_work_id: uuid.UUID

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now())
