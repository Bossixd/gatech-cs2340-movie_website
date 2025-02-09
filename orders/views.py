from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Order
from movies.models import Movie

from django.shortcuts import redirect

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
                    # 'cost': movie.cost,
                    'cost': 100
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
            order.price += movie.cost
            order.movies.add(movie)
        
        return redirect(request.META['HTTP_REFERER'])
