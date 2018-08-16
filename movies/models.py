from django.db import models

# Create your models here.


class Movie(models.Model):
    """
    Movie model

    Contains all required movie info
    """
    movie_uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class MovieCharacter(models.Model):
    """
    Movie character model

    p.s when data is small
    """
    character_uid = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
