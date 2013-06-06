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
    """ Display all demonstrations """
    demos = Demonstration.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'library/library.html', {'demos':demos})
    
def demonstrationView(request, id):
	"""Display a demonstration"""
	d = Demonstration.objects.get(id=id)
	d.views += 1
	d.save()
	sequents = d.sequents.split('<br/>')
	proof = d.content.split('\n')
	return render(request, 'library/demonstrationView.html', {'demo':d, 'sequents':sequents, 'proof':proof})
