__author__ = 'willflowers'

from django.contrib import admin

from .models import Movies, Rater, Ratings


class MoviesAdmin(admin.ModelAdmin):
    fields = ['title', 'genre']

class RatingsAdmin(admin.ModelAdmin):
    fields = ['movie', 'rater', 'rating']

class RaterAdmin(admin.ModelAdmin):
    fields = ['gender', 'age', 'occupation', 'zipcode']

admin.site.register(Movies)
admin.site.register(Ratings)
admin.site.register(Rater)