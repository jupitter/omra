from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "title": "Welcome To The Ordina Music Rater",
        "text": "Make yourself at home"
        }

    return render(request, 'song_rater/index.html', context)
