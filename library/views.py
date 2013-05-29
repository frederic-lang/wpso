#-*- coding: utf-8 -*-
from django.shortcuts import render
from library.models import Demonstration

def home(request):
  return render(request, 'base.html')

def doc(request):
  return render(request, 'library/doc.html')
 
def example(request):
  return render(request, 'library/example.html')

def show(request):
    """ Afficher tous les articles de notre blog """
    demos = Demonstration.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'library/library.html', {'demos':demos})
