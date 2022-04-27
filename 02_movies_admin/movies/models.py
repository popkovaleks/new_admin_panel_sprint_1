import uuid


from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField('name', max_length=255)

    description = models.TextField('description', blank=True)

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"genre"

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Filmwork(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField('title', max_length=255)

    description = models.TextField('description', blank=True)

    creation_date = models.DateField('creation_date', blank=True)

    rating = models.FloatField('rating', blank=True)


    class FilmworkType(models.TextChoices):
        MOVIE = 'movie'
        TV_SHOW = 'TV_SHOW'


    type = models.CharField(max_length=255, choices=FilmworkType.choices)

    created = models.DateTimeField(auto_now_add=True)

    modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "content\".\"film_work"

        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"

    def __str__(self):
        return self.title