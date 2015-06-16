__author__ = 'willflowers'
from django import forms
from django.contrib.auth.models import User
from .models import Rater, Ratings

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #hides password when typed

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class RaterForm(forms.ModelForm):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    gender = forms.Field( label="Gender", initial='',
                               widget=forms.Select(), required=True)


    )
    age = forms.Field( label="Age", initial='',
                                required=True)

    )
    job = forms.Field( label="Job", initial='',
                               required=True)

    class Meta:
        model = Rater
        fields = ('gender', 'age', 'job', 'zip_code')


class RatingForm(forms.ModelForm):
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

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               initial='',
                               widget=forms.Select(),
                               required=True)

    text_rating = forms.CharField(initial='None',
                                  required=False)


    class Meta:
        model = Rating
        fields = ('rating','text_rating')


class EditForm(forms.ModelForm):
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

    rating = forms.ChoiceField(choices=RATING_CHOICES,
                               label="Rating",
                               initial='',
                               widget=forms.Select(),
                               required=True)


    class Meta:
        model = Rating
        fields = ('rating','text_rating')


class DeleteForm(forms.ModelForm):
    class Meta:
        model = Rating
        exclude = ('rating', 'model', 'rater')