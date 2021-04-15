from django.db import models
import PIL

# Create your models here. - model = table in the database

# one class is a one table in the database


class Studio(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Anime(models.Model):
    # ability to change the score or create your own
    # null - default field empty
    # blank - can be empty, no value needed
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE, null=True, blank=True)
    name_eng = models.CharField(max_length=500, null=True)
    description = models.TextField(blank=True, null=True)
    num_episodes = models.IntegerField(blank=True, null=True)
    status = models.CharField(choices=[("Currently Airing", "Currently Airing"), ("Finished Airing", "Finished Airing")]
                              , max_length=256, null=True, blank=True)
    premiered = models.CharField(blank=True, null=True, max_length=256) # add choices like Winter Year
    source = models.CharField(blank=True, null=True, max_length=256) # add choices manga, novel, game, whatever
    genres = models.CharField(blank=True, null=True, max_length=256) # also create genres a lot of genres
    duration = models.CharField(blank=True, null=True, max_length=256) # add
    score = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=10)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name_eng

    # to change plural names on the view
    # class Meta:
    #     verbose_name = "Anime"
    #     verbose_name_plural = "Anime"
