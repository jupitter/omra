from django.shortcuts import render
from song_rater.models import Song
from django.views.generic.list import ListView


def index(request):
    context = {
        "title": "Welcome To The Ordina Music Rater",
        "text": "Make yourself at home"
    }

    return render(request, 'song_rater/index.html', context)


class SongListView(ListView):
    model = Song
