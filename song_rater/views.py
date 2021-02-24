from django.shortcuts import render, get_object_or_404, redirect
from song_rater.models import Song, Rating
from django.views.generic.list import ListView
from django.forms import modelform_factory
from django.views.generic.edit import CreateView


def index(request):
    context = {
        "title": "Welcome To The Ordina Music Rater",
        "text": "Make yourself at home"
    }

    return render(request, 'song_rater/index.html', context)


class SongListView(ListView):
    model = Song
    context_object_name = 'song_list'


RatingForm = modelform_factory(Rating, exclude=["song"])


def song_detail(request, id):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.song_id = id
            rating.save()
            return redirect("song_rater:song_list",)
    else:
        form = RatingForm()

    song = get_object_or_404(Song, pk=id)
    ratings_list = song.rating_set.all()
    context = {"details": song,
               "form": form,
               "all_ratings": ratings_list
               }

    return render(request, 'song_rater/song_detail.html', context)


class AddSong(CreateView):
    model = Song
    fields = ['title', 'artist']
    success_url = "/song_add_succes"


def add_song_successfully(request):
    return render(request, 'song_rater/song_add_succes.html')
