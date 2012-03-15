from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('flashcardapp.views',
    (r'^$', 'index'),
    (r'^create/$', 'create'),
    (r'^create/success/$', 'create_success'),
    (r'^(?P<flashcard_id>\d+)/create_question/$', 'create_question'),
    (r'^(?P<flashcard_id>\d+)/edit/$', 'edit'),
    (r'^(?P<flashcard_id>\d+)/$', 'view_flashcard'),
)
