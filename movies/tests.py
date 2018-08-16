from django.test import TestCase
from django.urls import reverse
from movies.models import Movie, MovieCharacter


def create_movie(uid):
    """
    Create Movie object with uid and name
    """
    return Movie.objects.create(movie_uid=uid, name='test movie')


def create_character(uid, movie):
    """
    Create Movie object with uid and name
    """
    return MovieCharacter.objects.create(character_uid=uid, name='test character', movie=movie)


class MoviesMainViewTests(TestCase):
    def test_no_movies(self):
        """
        If no movies exist, context is empty.
        """
        response = self.client.get(reverse('movies-list'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['movie_list'], [])

    def test_movies_add_and_index(self):
        """
        Test add movie and display on index page
        """
        create_movie(uid='2baf70d1-42bb-4437-b551-e5fed5a87abe')
        response = self.client.get(reverse('movies-list'))
        self.assertQuerysetEqual(
            response.context['movie_list'],
            ['<Movie: 2baf70d1-42bb-4437-b551-e5fed5a87abe>']
        )

    def test_movies_character_add(self):
        """
        Test add movie character and check count from movie _set object
        """
        movie = create_movie(uid='2baf70d1-42bb-4437-b551-e5fed5a87abe')
        create_character(uid='2baf70d1-42bb-4437-b551-e5fed5a87abe', movie=movie)
        movie_characters = movie.moviecharacter_set.all()
        self.assertCountEqual(
            [movie_characters.count()], [1]
        )
