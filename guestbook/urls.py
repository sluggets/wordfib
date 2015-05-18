from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^wordfib/', include('wordfib.urls', namespace='wordfib')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('wordfib.urls', namespace='wordfib')),
)
