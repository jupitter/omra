from django.test import TestCase
from django.urls import reverse

from .models import Song


class IndexViewTest(TestCase):
    def test_index(self):
        url = reverse('song_rater:index')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Ordina Music Rater")


class SongListTest(TestCase):
    def test_no_songs(self):
        url = reverse('song_rater:song_list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Sorry")

    def test_with_songs(self):
        song = Song(artist="test", title="test2")
        song.save()
        url = reverse('song_rater:song_list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "test2")


class AddSongTest(TestCase):
    def test_added_song(self):
        url = reverse('song_rater:add_song')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.client.post('/add_song', {"title": "testing123", 'artist': "artist123"})
        self.assertEqual(Song.objects.last().title, "testing123")
