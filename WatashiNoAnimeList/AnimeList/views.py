from django.http import HttpResponse
from django.shortcuts import render
from .models import Anime


# Create your views here.

def index(request):
    response = Anime.objects.all()
    # studio = Anime.objects.filter(studio=1)
    # studio = Anime.objects.filter(studio__isnull=True)
    # anime = Anime.objects.filter(description__icontains="lol")
    return HttpResponse(response)
