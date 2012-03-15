from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'main.views.home'),
    (r'^flashcard/', include('flashcardapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
