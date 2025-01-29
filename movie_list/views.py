from django.shortcuts import render

def movie_page(request):
    return render(request, 'movie_list/movie_page.html')