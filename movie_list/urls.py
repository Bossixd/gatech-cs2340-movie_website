from django.urls import path

import movies
from . import views

urlpatterns = [
    path('', views.movie_page, name='movie_page'),
]