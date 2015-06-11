__author__ = 'willflowers'

from django.shortcuts import render
from .models import Status
from django.http import HttpResponse


def all_statuses(request):
    statuses = Status.objects.all()
    return HttpResponse("Here are all the statuses.")