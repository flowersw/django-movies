__author__ = 'willflowers'

from django.db import models

# Create your models here.
class Rater(models.Model):
    gender = models.CharField(max_length=7)
    age = models.IntegerField()
    occupation = models.IntegerField()
    zipcode = models.CharField(max_length=12)



class Movies(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)


class Ratings(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movies)
    rating = models.IntegerField()
