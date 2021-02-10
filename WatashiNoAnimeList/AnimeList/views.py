from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime


# Create your views here.

def index(request):
    response = Anime.objects.all()
    return HttpResponse(response)
