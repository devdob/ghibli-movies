from django.db import models

# Create your models here.


class Movie(models.Model):
    """
    Movie model

    Contains all required movie info
    """
    movie_uid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.movie_uid


class MovieCharacter(models.Model):
    """
    Movie character model
    """
    character_uid = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.character_uid
