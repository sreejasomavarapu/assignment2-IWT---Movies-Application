from platform import release
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    hero = models.CharField(max_length=100)
    heroine = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField()
    img = models.ImageField()

    def __str__(self):
        return self.name
