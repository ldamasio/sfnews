from django.db import models


class Count(models.Model):
    count = models.IntegerField(default=0)


class Article(models.Model):
    uid = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)
    newssite = models.CharField(max_length=255)