#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'library.views.home'),
	url(r'^library/', include('library.urls')),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^logic/', include('logic.urls')),
	url(r'^about/', TemplateView.as_view(template_name="more/about.html")),
    # Examples:
    # url(r'^$', 'sog.views.home', name='home'),
    # url(r'^sog/', include('sog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
