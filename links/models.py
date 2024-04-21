from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    class LinkType(models.TextChoices):
        WEBSITE = "website", "website"
        BOOK = "book", "book"
        ARTICLE = "article", "article"
        MUSIC = "music", "music"
        VIDEO = "video", "video"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField()
    image_url = models.URLField(blank=True)
    type = models.CharField(max_length=7, choices=LinkType, default=LinkType.WEBSITE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    links = models.ManyToManyField(Link, through="LinkCollection", through_fields=("collection", "link"))


class LinkCollection(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
