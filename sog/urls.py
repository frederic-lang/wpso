#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'logic.views.home'),
	url(r'^accueil/$', 'logic.views.home'),
	url(r'^fishing/$', 'logic.views.fishing'),
	url(r'^doc/$', 'logic.views.doc'),
	url(r'^example/$', 'logic.views.example'),
    # Examples:
    # url(r'^$', 'sog.views.home', name='home'),
    # url(r'^sog/', include('sog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
