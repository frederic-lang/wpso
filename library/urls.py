#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('library.views',
	url(r'^list/$', 'show'),
	url(r'^demonstration/(\d+)/$', 'demonstrationView', name = 'dem'),
   	url(r'^doc/$', 'doc'),
	url(r'^example/$', 'example'),
	url(r'^$', 'home'),
	url(r'^home/$', 'home'),
    )
