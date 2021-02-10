from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class IndexViewTest(TestCase):
    def test_index(self):
        url = reverse('index')
        r = self.client.get(url)
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "Ordina Music Rater")