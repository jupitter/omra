from django.test import TestCase, Client
from django.urls import reverse

from .models import Song

# Create your tests here.
class IndexViewTest(TestCase):
    def test_index(self):
        url = reverse('song_rater:index')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Ordina Music Rater")

class SongListTest(TestCase):
    def test_no_songs(self):
        """If no songs exist, an appropriate message is displayed"""
        url = reverse('song_rater:song_list')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)


