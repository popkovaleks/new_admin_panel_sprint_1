from django.contrib import admin
from .models import Genre, Filmwork
# Register your models here.

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Filmwork)
class FilmworkAdmin(admin.ModelAdmin):
    pass