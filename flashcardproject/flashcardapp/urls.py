from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('flashcardapp.views',
    (r'^$', 'index'),
    (r'title/(?P<sub>\w+)/$', 'view_title'),
    (r'^create/$', 'create'),
    (r'^search/$', 'search'),
    (r'^(?P<flashcard_id>\d+)/create_question/$', 'create_question'),
    (r'^(?P<flashcard_id>\d+)/like/$', 'like'),
    (r'^(?P<flashcard_id>\d+)/edit/$', 'edit'),
    (r'^(?P<flashcard_id>\d+)/copy/$', 'copy'),
    (r'^(?P<flashcard_id>\d+)/delete/$', 'delete'),
    (r'^(?P<flashcard_id>\d+)/$', 'view_flashcard'),
)
