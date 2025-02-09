from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.IntegerField()
    movies = models.ManyToManyField(Movie)

    # def __str__(self):
    #     return f"Order for {self.movie.title} (Price: {self.price})"