from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from movies.forms import ReviewForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()  # Using the related_name defined in the model

    if request.method == 'POST':
        # Ensure the user is logged in; otherwise, you might want to redirect to a login page.
        if not request.user.is_authenticated:
            return redirect('login')  # Replace 'login' with your login URL name

        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user  # Assuming you want to record which user posted the review
            review.save()
            return redirect('movie_detail', pk=movie.pk)  # Redirect to avoid form resubmission
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'movie_list/movie_detail.html', context)
# def movie_detail(request):
#     return render(request, 'movie_list/movie_detail.html', {
#         "movies": [
#             {
#                 "title": "The Shawshank Redemption",
#                 "description": "The redemption of shank shank",
#             },
#             {
#                 "title": "The Godfather",
#                 "description": "The godfather so fatherly",
#             },
#             {
#                 "title": "The Dark Knight",
#                 "description": "The dark knight hits",
#             }
#         ]
#     })

