from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wordfib.views.home_page', name='home'),
    url(r'^from_def/', 'wordfib.views.home_page', {'from_def': True}, name='from_def'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scoreboard/', 'wordfib.views.scoreboard', name='scoreboard'),
    url(r'^vote/', 'wordfib.views.vote', name='vote'),
    url(r'^add_def/', 'wordfib.views.add_def', name='add_def'),
    url(r'^admin/', include(admin.site.urls)),
)
