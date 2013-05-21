#-*- coding: utf-8 -*-
from django import forms
 
class CallForm(forms.Form):
	title = forms.CharField(required = False)
	call = forms.CharField(widget=forms.Textarea)
	toBeSaved = forms.BooleanField(label = u'Save', required = False )


