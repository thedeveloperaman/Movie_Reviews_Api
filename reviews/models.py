from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    tmdb_id = models.IntegerField()
    movie_title = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie_title} review by {self.user.username}"
