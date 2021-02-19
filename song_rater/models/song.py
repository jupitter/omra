from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    artist = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} - {self.artist}"


RATING_CHOICES = [
    (1, "1 - Trash"),
    (2, "2 - Bad"),
    (3, "3 - Average"),
    (4, "4 - Great"),
    (5, "5 - Excellent"),
]


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
