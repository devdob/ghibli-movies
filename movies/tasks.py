from celery.task import task
import requests
from movies.models import Movie, MovieCharacter


@task
def gather_movie_data():
    """
    Task logic to gather movies data and save to DB
    :return:
    """
    r = requests.request('get', 'https://ghibliapi.herokuapp.com/films')
    for item in r.json():
        if not Movie.objects.filter(movie_uid=item['id']):
            movie = Movie(movie_uid=item['id'], name=item['title'])
            movie.save()
            if 'people' in item and len(item['people']) > 1:
                for person_url in item['people']:
                    try:
                        rp = requests.request('get', person_url).json()
                        if 'name' in rp:
                            mc = MovieCharacter(character_uid=rp['id'], name=rp['name'],
                                                movie=movie)
                            mc.save()
                    except Exception as e:
                        print(e)

