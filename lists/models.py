from django.db import models
from django.contrib.auth.models import User

class MovieList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_lists')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class MovieListItem(models.Model):
    movie_list = models.ForeignKey(MovieList, on_delete=models.CASCADE, related_name='items')
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} in {self.movie_list.name}"
