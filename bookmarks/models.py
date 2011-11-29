from django.db import models
from dalian.categories.models import Category

class Bookmark(models.Model):
    name = models.CharField(max_length = 50)
    url = models.URLField(unique = True)
    visited = models.IntegerField(default = 0)
    archive = models.BooleanField(default = False)
    category = models.ForeignKey(Category, related_name='bookmark_set')
