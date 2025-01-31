from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_page, name='movie_page'),
]