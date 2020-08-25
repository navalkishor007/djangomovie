from django.db import models

# Create your models here.

class input_movie(models.Model):
    name = models.CharField(max_length=30)
    rating = models.IntegerField()

