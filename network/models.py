from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class make_tweet(models.Model):
    # title=models.CharField(max_length=64)
    content=models.CharField(max_length=1000,null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="tweet")
    time_stamp=models.DateTimeField(auto_now_add=True)
    is_liked=models.ManyToManyField(User,related_name="like",blank=True)
    is_retweet=models.ManyToManyField(User,related_name="retweet",blank=True)
    img=models.ImageField(upload_to='uploads/% Y/% m/% d/')
    


class tweet_comment(models.Model):
    comment=models.CharField(max_length=1000,null=False)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name="comment")
    tweet=models.ForeignKey(make_tweet,on_delete=models.CASCADE,related_name="tweet")
    is_liked=models.ManyToManyField(User,related_name="comment_like",blank=True)
    timestamp=models.DateTimeField(auto_now_add=True)

class mutuals(models.Model):
    is_followed=models.ManyToManyField(User,related_name="follower",blank=True)