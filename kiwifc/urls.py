import os
import sys
from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'public.views.index', name='home'),
    # url(r'^kiwifc/', include('kiwifc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if 'runserver' in sys.argv or 'runserver_plus':
    urlpatterns += patterns('',  url(r'^media/(.*)$',
                                     'django.views.static.serve', kwargs={'document_root': settings.MEDIA_ROOT}), )
