#-*- coding: utf-8 -*-
from django import forms
 
class CallForm(forms.Form):
	call = forms.CharField(widget=forms.Textarea, required = False)
	toBeSaved = forms.BooleanField(label = u'Save', required = False )

class InformationForm(forms.Form):
	title = forms.CharField()
	comment = forms.CharField(widget=forms.Textarea, required = False)
	tags = forms.CharField(required = False)
