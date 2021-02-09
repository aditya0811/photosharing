
from django.db import models


class Meme(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    caption = models.CharField(max_length=500)

    def __str__(self):
        """A string representation of the model."""
        return self.name