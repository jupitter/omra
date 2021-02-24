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


class DetailViewTest(TestCase):
    def setUp(self):
        self.song = Song.objects.create(title="I Want To Know What Love Is", artist="Foreigner")

    def test_detail(self):
        url = reverse('song_rater:song_detail', kwargs={"id": self.song.id})
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "I Want To Know What Love Is")
