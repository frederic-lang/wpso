#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout, login

urlpatterns = patterns('accounts.views',
	url(r'^profile/$', 'profileView'),
	url(r'^login/$', login),
	url(r'^logout/$', logout),
	url(r'^register/$', 'register'),

    )
