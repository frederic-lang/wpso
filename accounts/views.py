#-*- coding: utf-8 -*-
from django.shortcuts import render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
		username = form.clean_username()
            	password = form.clean_password2()
		form.save()
		user = authenticate(username=username,
                                password=password)
            	login(request, user)
            	return HttpResponseRedirect("/library/home/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profileView(request):
	return render(request, "registration/profile.html")



