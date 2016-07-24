from django.db import models

class people(models.Model):
    
        title = models.CharField(max_length=250)
        body = models.TextField()

