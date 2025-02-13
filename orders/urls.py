from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path('add/<int:movie_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:movie_id>/', views.remove_cart, name='remove_cart'),
    path('checkout/<int:order_id>/', views.checkout, name='checkout'),
    path('', views.orders, name='orders'),
]