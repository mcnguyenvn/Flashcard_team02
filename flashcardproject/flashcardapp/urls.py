from django.conf.urls.defaults import patterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('flashcardapp.views',
    (r'^$', 'index'),
<<<<<<< HEAD
    (r'^title/(?P<sub>\w+)/$', 'view_title'),
    (r'^create/$', 'create'),
    (r'^create/success/$', 'creatingsuccess'),
    (r'^edit/success/$', 'creatingsuccess'),
=======
    (r'^create/$', 'create'),
    (r'^create/success/$', 'creatingsuccess'),
>>>>>>> c64d101212f1ab4060c9ca4390c56bdd4c0432b3
    (r'^(?P<flashcard_id>\d+)/create_question/$', 'create_question'),
    (r'^(?P<flashcard_id>\d+)/edit/$', 'edit'),
    (r'^(?P<flashcard_id>\d+)/$', 'view_flashcard'),
)
