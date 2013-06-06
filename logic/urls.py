#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout, login

urlpatterns = patterns('logic.views',
	url(r'^fishing/$', 'fishing'),
	url(r'^save/$', 'save'),
    )
