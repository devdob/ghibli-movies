from django.views.generic import ListView
from .models import Movie

from movies.tasks import gather_movie_data

# Create your views here.


class MovieList(ListView):
    """
    Main view to get list of Movie objects
    """
    model = Movie
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # gather_movie_data()
        context['movie_list'] = Movie.objects.all()
        return context
