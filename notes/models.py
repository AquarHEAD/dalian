from django.db import models

class Note(models.Model):
    name = models.CharField(max_length = 200)
    content = models.TextField()
    lang = models.CharField(max_length = 50, blank = True)
    password = models.CharField(max_length = 30, blank = True)
    private = models.BooleanField(default = False)
    modified = models.DateTimeField(auto_now = True)