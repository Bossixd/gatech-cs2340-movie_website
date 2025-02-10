from django.db import models
from movies.models import Movie
from django.contrib.auth.models import User

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.FloatField()
    movies = models.ManyToManyField(Movie)
    ordered = models.BooleanField(default=False)
    #ordered if for like checkout, not sure how it would be implemented yet

    def __str__(self):
        return f"Order for {self.user.username} (Ordered: {self.ordered})"