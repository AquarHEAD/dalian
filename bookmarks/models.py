from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 200)

class Bookmark(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField()
    visited = models.IntegerField(default = 0)
    archive = models.BooleanField(default = False)
    category = models.ForeignKey('Category')