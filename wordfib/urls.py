from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'wordfib.views.home_page', name='home'),
    url(r'^from_def/', 'wordfib.views.home_page', {'from_def': True}, name='from_def'),
    url(r'^blank_name', 'wordfib.views.home_page', {'name_error': True}, name='blank_name'),
    url(r'^blank_choice', 'wordfib.views.home_page', {'choice_error': True}, name='blank_choice'),
    url(r'^self_voter', 'wordfib.views.home_page', {'self_error': True}, name='self_voter'),
    url(r'^add_another/', 'wordfib.views.add_another', name='add_another'),
    url(r'^add_yet_another/', 'wordfib.views.add_another', {'pop_again': True}, name='add_yet_another'),
    url(r'^from_add/', 'wordfib.views.add_def', {'from_add_another': True}, name='from_add'),
    url(r'^scoreboard/', 'wordfib.views.scoreboard', name='scoreboard'),
    url(r'^vote/', 'wordfib.views.vote', name='vote'),
    url(r'^add_def/', 'wordfib.views.add_def', name='add_def'),
)
