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
        song = Song(author="test", title="test2")
        song.save()
        url = reverse('song_rater:song_list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "test2")
