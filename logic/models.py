#-*- coding: utf-8 -*-
from django.db import models
 
class Demonstration(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
 
    def __unicode__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
    	return u"%s" % self.title
