#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from logic.forms import CallForm, InformationForm
from logic.engine.compiler import Compiler
from library.models import Demonstration
from django.contrib.auth.decorators import login_required
from django.http import Http404
from library.views import demonstrationView


def fishing(request):
	if 'compiler' in request.session :
		c = request.session['compiler']
	else :
		request.session['compiler'] = Compiler()
		c = request.session['compiler']	
	if request.method == 'POST':  # S'il s'agit d'une requête POST
		form = CallForm(request.POST)  # Nous reprenons les données
                if form.is_valid(): # Nous vérifions que les données envoyées sont valides
			# Ici nous pouvons traiter les données du formulaire
			call = form.cleaned_data['call']
			c.setText(call)
			if c.compileSuccessfully() :
				if form.cleaned_data['toBeSaved'] :
					if c.couldBeFinished() :
						return redirect('logic.views.save')
					else :
						comment = "You can't save your Proof, it isn't finished !"
				else :
					comment = "Successfully compiled !"
			else :
 	    			comment = c.getError()
 	    	else : 
 	    		comment = "erreur dans le formulaire"
	else: # Si ce n'est pas du POST, c'est probablement une requête GET
		comment = "Start your proof here "
        	form = CallForm({'call':c.getText()}) # on récupère le brouillon s'il existe
        sequents = c.getSequentsPrinted() 
        request.session['compiler'] = c
        return render(request, 'logic/fishing.html', {'sequents' : sequents, 'comment' : comment, 'form' : form })

@login_required
def save(request) :
	if 'compiler' in request.session :
		c = request.session['compiler']
	else :
		raise Http404
	lemma = c.getConclusion()
	content = c.getText()
	sequents = c.getSequentsPrinted()
	if request.method == 'GET' :
		form = InformationForm()
		return render(request, 'logic/save.html', { 'lemma' : lemma , 'form' : form, 'sequents' : sequents})
	elif request.method == 'POST' :
		form = InformationForm(request.POST) 
                if form.is_valid(): 
			title = form.cleaned_data['title']
			tags = form.cleaned_data['tags']
			comment = form.cleaned_data['comment']
			saved_demo = Demonstration(title = title,
						   content = content, 
						   lemma = lemma, 
						   author = request.user, 
						   views = 1,
						   sequents = '<br/>'.join(sequents),
						   tags = tags,
						   comment = comment,
						   official = False)
			saved_demo.save()
			url = '/library/demonstration/' + str(saved_demo.id) + '/'
			return redirect(url)
		else :
			return render(request, 'logic/save.html', { 'lemma' : lemma, 'form' : form, 'sequents' : sequents })
	else : 
		raise Http404
