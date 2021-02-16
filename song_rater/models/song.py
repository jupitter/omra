from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} - {self.artist}"
