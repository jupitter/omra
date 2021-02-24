from django.urls import path
from . import views

app_name = "song_rater"

urlpatterns = [
    path('', views.index, name='index'),
    path('song_list', views.SongListView.as_view(), name='song_list'),
    path('song_details/<int:id>', views.song_detail, name='song_detail'),
    path('add_song', views.AddSong.as_view(), name='add_song'),
    path('song_add_succes', views.add_song_successfully, name="add_song_successfully")
]
