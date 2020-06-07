from django.db import models
from django.conf import settings
import random


USER = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    objects = None
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ['-id']


    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 153)
        }
