from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.db import models

# Create your models here.

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,blank = False,null=True)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
    updated = models.DateTimeField(auto_now_add = False, auto_now=True)

    def __unicode__(self):
        return self.email



class Album(models.Model):
    location = models.CharField(max_length=250)
    path = models.CharField(max_length=500)
    driver = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    photo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.location + ' : ' + self.path



class Song(models.Model):
    location = models.ForeignKey(Album, on_delete=models.CASCADE)
    time = models.CharField(max_length=10)
    station = models.CharField(max_length=250)
    is_full = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.location_id})

    def __str__(self):
        return self.station

