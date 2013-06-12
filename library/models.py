#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Demonstration(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    content = models.TextField(blank=True)
    lemma = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    comment = models.TextField(blank=True)
    tags = models.CharField(max_length=100)
    sequents = models.TextField(blank=True)
    views = models.IntegerField()
    official = models.BooleanField()
    roots = models.CharField(max_length=200)
    lemmaNode = models.TextField()
    
    def __unicode__(self):
    	return u"%s" % self.title
