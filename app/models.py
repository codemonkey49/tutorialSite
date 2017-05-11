from __future__ import unicode_literals

from django.db import models

# Create your models here.
class componentModel(models.Model):
    #compID=models.AutoField(primary_key=True)
    componentType=models.CharField(max_length=100)
    order=models.IntegerField()
    componentContent=models.CharField(max_length=10000,blank=True,null=True)
    image=models.CharField(max_length=500,blank=True,null=True)
    imageCaption=models.CharField(max_length=1000,blank=True,null=True)
    def __str__(self):              # __unicode__ on Python 2
        return str(self.componentType)

class tutorialModel(models.Model):
    title=models.CharField(max_length=100,unique=True)
    component=models.ManyToManyField(componentModel)
    def __str__(self):              # __unicode__ on Python 2
        return self.title