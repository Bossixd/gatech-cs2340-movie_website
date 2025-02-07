from django.urls import path
from .views import movie_detail, movie_list

app_name = "movie_list"
urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
]