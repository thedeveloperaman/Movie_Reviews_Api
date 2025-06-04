from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class SavedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_movies')
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=255)
    poster_path = models.CharField(max_length=255, blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.tmdb_id}) saved by {self.user.username}"
