from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('movie_title', 'price', 'movie')
    search_fields = ('movie_title', 'price')

    def movie_title(self, obj) :
        return obj.movie.title
    
    def movie_release_date(self, obj) :
        return obj.movie.release_date