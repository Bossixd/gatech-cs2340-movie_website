from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_list', 'user', 'price')
    search_fields = ('price',)
    filter_horizontal = ('movies',)
    
    def movie_list(self, obj):
        return list(obj.movies.all())

    def movie_title(self, obj) :
        return obj.movie.title
    
    def movie_release_date(self, obj) :
        return obj.movie.release_date