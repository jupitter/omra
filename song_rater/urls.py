from django.urls import path

from . import views

app_name = "song_rater"

urlpatterns = [
    path('', views.index, name='index'),
    path('song_list', views.SongListView.as_view(), name='song_list'),
]
