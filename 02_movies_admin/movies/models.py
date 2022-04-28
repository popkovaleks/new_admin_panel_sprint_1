import uuid


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):

    name = models.CharField('name', max_length=255)

    description = models.TextField('description', blank=True)

    class Meta:
        db_table = "content\".\"genre"

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):

    title = models.CharField('title', max_length=255)

    description = models.TextField('description', blank=True)

    creation_date = models.DateField('creation_date', blank=True)

    rating = models.FloatField('rating', blank=True, validators=[MinValueValidator(0), MaxValueValidator(0)])


    class FilmworkType(models.TextChoices):
        MOVIE = 'movie'
        TV_SHOW = 'TV_SHOW'


    type = models.CharField(max_length=255, choices=FilmworkType.choices)

    genres = models.ManyToManyField(Genre, through='GenreFilmwork')


    class Meta:
        db_table = "content\".\"film_work"

        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"


    def __str__(self):
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)

    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "content\".\"genre_film_work"