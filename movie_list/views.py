from django.shortcuts import render

def movie_page(request):
    return render(request, 'movie_list/movie_page.html', {
        "movies": [
            {
                "title": "The Shawshank Redemption",
                "description": "The redemption of shank shank",
            },
            {
                "title": "The Godfather",
                "description": "The godfather so fatherly",
            },
            {
                "title": "The Dark Knight",
                "description": "The dark knight hits",
            }
        ]
    })
