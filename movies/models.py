from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional: associate review with a user
    rating = models.PositiveIntegerField()  # e.g., a rating out of 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.movie.title} by {self.user.username}"