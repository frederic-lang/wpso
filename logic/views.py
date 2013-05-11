#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
from logic.forms import CallForm
from logic.parser import yacc_parse
 
def home(request):
  return render(request, 'home.html', {'current_date': datetime.now()})


 
def fishing(request):
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CallForm(request.POST)  # Nous reprenons les données
 
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
 
            # Ici nous pouvons traiter les données du formulaire
            author = form.cleaned_data['author']
            call = form.cleaned_data['call']
 	    dem = yacc_parse(call)

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
        form = CallForm()  # Nous créons un formulaire vide
 
    return render(request, 'fishing.html', locals())
