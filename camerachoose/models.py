__author__ = 'Jike'
from django.db import models


class Camera(models.Model):
    model = models.CharField(max_length=200)
    date = models.DateField()
    def __unicode__(self):
        return self.model
    def __str__(self):
        return self.model
# Create your models here.
