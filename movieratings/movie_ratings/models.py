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

from django.db import models
import operator
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
# Create your models here.

class Rater(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              null=True)


    )
    age = models.IntegerField()


    )
    job=models.CharField(default=0,
                            null=True)

    zip_code = models.CharField(max_length=10,
                              null=True)

    user = models.OneToOneField(User, null=True)

    def num_reviews(self):
        #add if ratings
        return self.rating_set.count()

    def movies_seen(self):
        #add if ratings
        ratings = self.rating_set.all()
        return {rating.movie: rating.rating for rating in ratings}

    @property
    def average_rating(self):
        #add if ratings:
        ratings = self.rating_set.all()
        total = 0
        if ratings:
            for rating in ratings:
                total += rating.rating
            return round(total/len(ratings), 2)
        else:
            return "No ratings"

    @property
    def ratings_count(self):
        count_rating = self.rating_set.all().aggregate(Count('rating'))
        if count_rating:
            return (count_rating['rating__count'])
        else:
            return "No ratings"

    def __str__(self):
        return "UserID: {} || {} || {} || zip: {} || job: {}".format(self.id , self.gender, self.age, self.zip_code,
                                                                     self.job)


class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)
    genre = models.ManyToManyField("Genre")

    def __str__(self):
        return self.title

    @property
    def average_rating(self):
        average_rating = self.rating_set.all().aggregate(Avg('rating'))
        if average_rating:
            return round(average_rating['rating__avg'], 2)
        else:
            return "No ratings"

    @property
    def ratings_count(self):
        count_rating = self.rating_set.all().aggregate(Count('rating'))
        if count_rating:
            return (count_rating['rating__count'])
        else:
            return "No ratings"


class Genre(models.Model):
    ACTION = "Action"
    ADVENTURE = "Adventure"
    ANIMATION = "Animation"
    CHILDREN = "Children's"
    COMEDY = "Comedy"
    CRIME = "Crime"
    DOCUMENTARY = "Documentary"
    DRAMA = "Drama"
    FANTASY = "Fantasy"
    FILM_NOIR = "Film-Noir"
    HORROR = "Horror"
    MUSICAL = "Musical"
    MYSTERY = "Mystery"
    ROMANCE = "Romance"
    SCIFI = "Sci-Fi"
    THRILLER = "Thriller"
    WAR = "War"
    WESTERN = "Western"
    GENRE_CHOICES = (
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (ANIMATION, "Animation"),
        (CHILDREN, "Children's"),
        (COMEDY, "Comedy"),
        (CRIME, "Crime"),
        (DOCUMENTARY, "Documentary"),
        (DRAMA, "Drama"),
        (FANTASY, "Fantasy"),
        (FILM_NOIR, "Film-Noir"),
        (HORROR, "Horror"),
        (MUSICAL, "Musical"),
        (MYSTERY, "Mystery"),
        (ROMANCE, "Romance"),
        (SCIFI, "Sci-Fi"),
        (THRILLER, "Thriller"),
        (WAR, "War"),
        (WESTERN, "Western")
    )

    genre = models.CharField(choices=GENRE_CHOICES,
                             null=True,
                             max_length=30)

    def __str__(self):
        return self.genre


def one_to_five(value):
    if value not in [1, 2, 3, 4, 5]:
        return ValidationError


class Rating(models.Model):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    RATING_CHOICES=(
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5)
    )

    rating = models.IntegerField(choices=RATING_CHOICES,
                                 null=True,
                                 validators=[one_to_five])

    movie = models.ForeignKey(Movie, null=True)

    rater = models.ForeignKey(Rater, null=True)

    posted_at = models.DateTimeField(null=True)

    text_rating = models.CharField(max_length=255, null=True)

    def __str__(self):
        return "{} reviewed {} || {} * rating.".format(self.rater.id, self.movie.title, self.rating)

    class Meta:
        unique_together = ('rater', 'movie')


def create_users():
    for rater in Rater.objects.all():
        user = User.objects.create_user('User{}'.format(rater.id),
                                        'user{}@example.com'.format(rater.id),
                                        'password'.format(rater.id))
        password = "password"
        user.set_password(password)
        user.save()
        rater.user = user
        rater.save()


def change_emails():
    for user in User.objects.all():
        password = "password"
        user.set_password(password)
        user.save()

def delete_users():
    for user in User.objects.all():
        user.delete()



