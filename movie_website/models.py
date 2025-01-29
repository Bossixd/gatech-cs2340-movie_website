from django.db import models

from django.contrib.postgres.fields import ArrayField

class Movie(models.Model):
    movieName = models.CharField(maxlength=200)

    def __str__(self):
        return self.movieName