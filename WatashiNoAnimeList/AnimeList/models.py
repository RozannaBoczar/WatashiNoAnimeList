from django.db import models


# Create your models here. - model = table in the database

# one class is a one table in the database

class Studio(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    # null - default field empty
    # blank - can be empty, no value needed
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=True, null=True)
    num_episodes = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    # to change plural names on the view
    # class Meta:
    #     verbose_name = "Anime"
    #     verbose_name_plural = "Anime"
