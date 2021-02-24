from django.shortcuts import render, get_object_or_404, redirect
from song_rater.models import Song, Rating
from django.views.generic.list import ListView
from django.forms import modelform_factory


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
            return redirect("song_rater:song_list")
    else:
        form = RatingForm()

    context = {"details": get_object_or_404(Song, pk=id),
               "form": form,
               }

    return render(request, 'song_rater/song_detail.html', context)
