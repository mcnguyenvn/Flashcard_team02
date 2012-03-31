from django.conf.urls.defaults import patterns, url

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('account.views',
    (r'^flashcardlist/$', 'user_flashcard'),
    (r'^profile/$', 'user_profile'),
    (r'^changepassword/$', 'change_password'),
)

urlpatterns += staticfiles_urlpatterns()
