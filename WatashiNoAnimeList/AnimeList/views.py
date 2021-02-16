from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

def index(request):
    response = Anime.objects.all()
    data = {'animes': response}
    # studio = Anime.objects.filter(studio=1)
    # studio = Anime.objects.filter(studio__isnull=True)
    # anime = Anime.objects.filter(description__icontains="lol")
    # return HttpResponse(response)
    return render(request, 'main.html', data)


def studio(request, id):
    studio_user = Studio.objects.get(pk=id)
    data = {"studio_user": studio_user}
    return render(request, "studio.html", data)


def anime(request, id):
    anime_user = Anime.objects.get(pk=id)
    response = Anime.objects.all()
    data = {"anime_user": anime_user, "animes": response}
    return render(request, "anime.html", data)
