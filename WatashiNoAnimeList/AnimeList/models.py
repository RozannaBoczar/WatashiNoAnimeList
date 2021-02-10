from django.db import models


# Create your models here.

# one class is a one table in the database

class Anime(models.Model):
    name = models.CharField(max_length=500, default="Anime")
    description = models.TextField(blank=True)
    num_episodes = models.IntegerField(default=12)
    year = models.IntegerField(default=2000)

    def __str__(self):
        return self.name
