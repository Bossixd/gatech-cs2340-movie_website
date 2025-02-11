from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from movies.forms import ReviewForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # Replace 'login' with your login URL name

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_list:movie_detail', pk=movie.pk)  # Use namespace
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'movie_list/movie_detail.html', context)