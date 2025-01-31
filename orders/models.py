from django.db import models
from movies.models import Movie

class Order(models.Model):
    price = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order for {self.movie.title} (Price: {self.price})"