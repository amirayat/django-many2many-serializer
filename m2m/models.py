from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)
    text = models.CharField(max_length=100)

class Post(models.Model):
    tag = models.ManyToManyField(Tag, related_name='poststag')
    text = models.CharField(max_length=100)