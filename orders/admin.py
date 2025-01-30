from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.OrderAdmin):
    list_display = ('movie_title', 'price', 'movie')
    search_fields = ('movie_title', 'price')
    list_filter = ('movie_release_date',)

    def movie_title(self, obj) :
        return obj.movie.title
    
    def movie_release_date(self, obj) :
        return obj.movie.release_date