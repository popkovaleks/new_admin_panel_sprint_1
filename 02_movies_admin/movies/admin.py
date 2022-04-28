from django.contrib import admin
from .models import Genre, Filmwork, Person, GenreFilmwork, PersonFilmwork
# Register your models here.

class GenreFilmworkInline(admin.TabularInline):
    model = GenreFilmwork


class PersonFilmworkInline(admin.TabularInline):
    model = PersonFilmwork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

    search_fields = ('id', 'name',)


@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmworkInline, PersonFilmworkInline)

    list_display = ('title', 'type', 'creation_date', 'rating',)

    list_filter = ('type',)

    search_fields = ('title', 'description', 'id', )


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

    search_fields = ('id', 'full_name',)

