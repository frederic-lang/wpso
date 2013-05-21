#-*- coding: utf-8 -*-
from django.shortcuts import render
from library.models import Demonstration

def home(request):
  return render(request, 'home.html')

def doc(request):
  return render(request, 'doc.html')
 
def example(request):
  return render(request, 'example.html')

def show(request):
    """ Afficher tous les articles de notre blog """
    demos = Demonstration.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'library.html', {'demos':demos})
