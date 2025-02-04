from django.urls import path
from .views import movie_detail, movie_list

import movies
from . import views

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
]