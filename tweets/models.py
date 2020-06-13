from django.db import models
from django.conf import settings
import random


User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    # Maps to SQL data
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Many users can have many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    objects = None
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-id']


    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 153)
        }
