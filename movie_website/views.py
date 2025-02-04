from django.views.generic import ListView

from movies.models import Movie


class SearchView(ListView):
    model = Movie
    template_name = 'movie_list/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(title__icontains=query)
        return object_list

