from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'reviews')
    search_fields = ('title', 'description')
    list_filter = ('release_date',)