#-*- coding: utf-8 -*-
from django.shortcuts import render
from logic.forms import CallForm
from logic.mathplus.compiler import Compiler
from library.models import Demonstration
 
def fishing(request):
    c = Compiler()
    if request.method == 'POST':  # S'il s'agit d'une requête POST
        form = CallForm(request.POST)  # Nous reprenons les données
        
        if form.is_valid(): # Nous vérifions que les données envoyées sont valides
 
            # Ici nous pouvons traiter les données du formulaire
            call = form.cleaned_data['call']
            tit = form.cleaned_data['title']
            request.user.draft = call # pour enregistrer le "brouillon" d'un utilisateur
            c.setText(call)
 	    if c.compileSuccessfully() :
 	    	sequents = c.getSequentsPrinted()
 	    	comment = "Successfully compiled !"
 	    else :
 	    	comment = c.getError()
 	    	sequents = c.getSequentsPrinted()
 	    	
 	    if form.cleaned_data['toBeSaved'] == True :
 	    	saved_demo = Demonstration(title = tit, author = request.user.username, content = call, lemma = c.getConclusion())
 	    	saved_demo.save()

    else: # Si ce n'est pas du POST, c'est probablement une requête GET
    	sequents = c.getSequentsPrinted
    	comment = "Start your proof here "
        try :
        	form = CallForm(call = request.user.draft) # on récupère le brouillon s'il existe
        except :
        	form = CallForm()  # Nous créons un formulaire vide

 
    return render(request, 'fishing.html', {'sequents' : sequents, 'comment' : comment, 'form' : form })
