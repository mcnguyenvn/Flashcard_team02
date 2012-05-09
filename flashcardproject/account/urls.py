from django.conf.urls.defaults import patterns

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('account.views',
    (r'^(\w+)/flashcardlist/$', 'user_flashcard'),
    (r'^(\w+)/edit/$', 'edit_profile'),
    (r'^(\w+)/$', 'view_profile'),
    (r'^(\w+)/changepassword/$', 'change_password'),
)

urlpatterns += staticfiles_urlpatterns()
