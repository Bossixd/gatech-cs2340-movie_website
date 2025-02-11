from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Order
from movies.models import Movie
from django.contrib import messages

from django.shortcuts import redirect

from datetime import date

@login_required(login_url='auths:login')
def orders(request):
    if request.method == "GET":
        orders = Order.objects.filter(user=request.user).all()

        args = {
            'orders': []
        }

        for order in orders:
            movies = []
            for movie in order.movies.all():
                movies.append({
                    'title': movie.title,
                     'cost': movie.price,
                    'id': movie.id,
                })
            args['orders'].append({
                'date': order.date,
                'cost': order.price,
                'id': order.id,
                'movies': movies
            })

        return render(request, 'orders/orders.html', args)

    elif request.method == "POST":
        """
            Usage:
                date: date of order
                movies: list of movie titles
        """
        print(request.POST)
        user = request.user
        date = request.POST['date']
        movies = request.POST.getlist('movies')

        order = Order.objects.create(user=user, date=date)

        order.price = 0

        for movie_title in movies:
            movie = Movie.objects.get(title=movie_title)
            order.price += movie.get_price()
            order.movies.add(movie)

        return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='auths:login')
def add_cart(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    order, created = Order.objects.get_or_create(user=request.user, ordered=False,
                                                 defaults={'price': 0.0}, date=date.today()
                                                 )

    if movie not in order.movies.all():
        order.movies.add(movie)
        recalculate_price(order)
        order.save()

    return redirect('movie_list:movie_list')

@login_required(login_url='auths:login')
def remove_cart(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    try:
        order = Order.objects.get(user=request.user, ordered=False)
    except Order.DoesNotExist:
        price = 0
        messages.info(request, 'You do not have an active cart')

    if movie in order.movies.all():
        order.movies.remove(movie)
        recalculate_price(order)
        order.save()
        messages.info(request, 'You have removed {moive.title} from you cart')
    else:
        messages.info(request, '{movie.title} is not in your cart')

    return redirect('orders:orders')

def recalculate_price(order):
    adjustedPrice = 0
    for movie in order.movies.all():
        adjustedPrice += movie.get_price()
    order.price = adjustedPrice
    order.save()