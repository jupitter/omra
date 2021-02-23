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
    context_object_name = 'song_list'

def add_song(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('artist'):
            add_song = Song()
            add_song.title = request.POST.get('title')
            add_song.artist = request.POST.get('artist')
            add_song.save()
            return render(request, 'song_rater/add_song.html')
    else:
        return render(request, 'song_rater/add_song.html')
