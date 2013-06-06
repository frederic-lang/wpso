#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Demonstration(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    content = models.TextField()
    lemma = models.TextField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    comment = models.TextField(null=True)
    tags = models.TextField(null=True)
    sequents = models.TextField()
    views = models.IntegerField()
    official = models.BooleanField()
 
    def __unicode__(self):
    	return u"%s" % self.title
