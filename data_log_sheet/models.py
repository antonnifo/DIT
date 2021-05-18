from django.db import models


class DataLogSheet(models.Model):

    reel = models.CharField(max_length=200)
    epi  = models.IntegerField()
    scn  = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    clips = models.CharField(max_length=200)
    shot = models.IntegerField()
    take = models.IntegerField()
    note = models.CharField(max_length=200)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)   

    class Meta:
        ordering = ('epi',)     