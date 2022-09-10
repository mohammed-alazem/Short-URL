'''
Url shortener model
'''

from django.db import models
from .utils import create_shortened_url


# Create your models here.

class Shortener(models.Model):
    CreatedDate = models.DateTimeField(auto_now_add=True)
    LongURL = models.URLField()
    ShortURL = models.CharField(max_length=15, unique=True, blank=True)
    UsedCount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.LongURL} to {self.ShortURL}'

    def save(self, *args, **kwargs):
        # If the short url wasn't specified
        if not self.ShortURL:
            # We pass the model instance that is being saved
            self.ShortURL = create_shortened_url(self)

        super().save(*args, **kwargs)
