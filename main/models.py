from datetime import datetime
from django.db import models

# Create your models here.


class shortUrl(models.Model):

    longUrl = models.URLField()
    shortUrl = models.URLField()
    time = models.TimeField(auto_now=True)


    def __str__(self):
        return self.shortUrl