from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from movies.models import Movie
from movies.models import Review
from movies.forms import ReviewForm
from django.http import HttpResponseForbidden

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


@login_required
def edit_review(request, review_id):
    # Retrieve the review or return 404 if it doesn't exist.
    review = get_object_or_404(Review, id=review_id)

    # Ensure that the current user is the author of the review.
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this review.")

    if request.method == 'POST':
        # Bind the form to the existing review instance.
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            # Redirect to the movie detail page after successful edit.
            return redirect('movie_detail', pk=review.movie.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'movie_list/edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):
    # Retrieve the review or return 404 if it doesn't exist.
    review = get_object_or_404(Review, id=review_id)

    # Ensure that the current user is the author of the review.
    if review.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this review.")

    if request.method == 'POST':
        # Save the movie’s primary key so you can redirect after deletion.
        movie_pk = review.movie.pk
        review.delete()
        # Redirect to the movie detail page after deletion.
        return redirect('movie_detail', pk=movie_pk)

    # Render a confirmation page if the request method is GET.
    return render(request, 'movie_list/confirm_delete.html', {'review': review})