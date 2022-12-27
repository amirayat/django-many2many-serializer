from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)

class Post(models.Model):
    tag = models.ManyToManyField(Tag)
    text = models.CharField(max_length=100)
