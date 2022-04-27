import uuid


from django.db import models

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

    rating = models.FloatField('rating', blank=True)


    class FilmworkType(models.TextChoices):
        MOVIE = 'movie'
        TV_SHOW = 'TV_SHOW'


    type = models.CharField(max_length=255, choices=FilmworkType.choices)


    class Meta:
        db_table = "content\".\"film_work"

        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"


    def __str__(self):
        return self.title