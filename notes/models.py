from django.db import models

class Note(models.Model):
    name = models.CharField(max_length = 200, blank = True)
    content = models.TextField()
    lang = models.CharField(max_length = 50, blank = True)