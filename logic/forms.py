#-*- coding: utf-8 -*-
from django import forms
 
class CallForm(forms.Form):
    author = forms.CharField(max_length=100)
    call = forms.CharField(widget=forms.Textarea)


