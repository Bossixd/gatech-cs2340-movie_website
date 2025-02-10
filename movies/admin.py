from django.contrib import admin
from .models import Movie, Review

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration', 'price')
    search_fields = ('title', 'description')
    list_filter = ('release_date',)

    def get_reviews(self, obj):
        return ":: ".join([review.comment for review in obj.reviews.all()[:3]])


@admin.register(Review)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating','comment')
    list_filter = ('movie','rating','user','created_at')
    search_fields = ('movie', 'user','comment')