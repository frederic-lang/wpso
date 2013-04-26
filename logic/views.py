#-*- coding: utf-8 -*-
from datetime import datetime
from django.shortcuts import render
 
def home(request):
  return render(request, 'home.html', {'current_date': datetime.now()})
  
  
