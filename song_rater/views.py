from django.shortcuts import render, get_object_or_404
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
    context_object_name = 'song_list'

def song_detail(request, id):
    context = {"details": get_object_or_404(Song, pk=id),
    }

    return render(request, 'song_rater/song_detail.html', context)

