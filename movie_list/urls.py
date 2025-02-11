from django.urls import path
from .views import movie_detail, movie_list, edit_review, delete_review

urlpatterns = [
    path('', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('reviews/edit/<int:review_id>/', edit_review, name='edit_review'),
    path('reviews/delete/<int:review_id>/', delete_review, name='delete_review'),
]