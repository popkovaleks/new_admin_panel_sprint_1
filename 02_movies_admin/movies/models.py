from tabnanny import verbose
import uuid


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

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

    name = models.CharField(_('name'), max_length=255)

    description = models.TextField(_('description'), blank=True)

    class Meta:
        db_table = "content\".\"genre"

        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):

    title = models.CharField(_('title'), max_length=255)

    description = models.TextField(_('description'), blank=True)

    creation_date = models.DateField(_('creation date'), blank=True)

    rating = models.FloatField(_('rating'), blank=True, validators=[MinValueValidator(0), MaxValueValidator(0)])


    class FilmworkType(models.TextChoices):
        MOVIE = 'M', _('Movie')
        TV_SHOW = 'TV', _('TV show')


    type = models.CharField(_('type'), max_length=2, choices=FilmworkType.choices)

    genres = models.ManyToManyField(Genre, through='GenreFilmwork')

    certificate = models.CharField(_('certificate'), max_length=512, blank=True)

    file_path = models.FileField(_('file'), blank=True, null=True, upload_to='movies/')


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

        verbose_name = _('Genre Filmwork')
        verbose_name_plural = _('Genres Filmworks')


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.TextField(_("full name"))

    film_work = models.ManyToManyField(Filmwork, through='PersonFilmwork')

    class Meta:
        db_table = "content\".\"person"

        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return self.full_name


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey('Filmwork', on_delete=models.CASCADE)

    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    role = models.TextField(_('role'), null=True)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"

        verbose_name = _('person of filmwork')
        verbose_name_plural = _('persons of filmwork')