from django.conf.urls.defaults import patterns, include, url
from views import *

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_flashcards.views.home', name='home'),
    # url(r'^django_flashcards/', include('django_flashcards.foo.urls')),
	url(r'^$',main_page),
    url(r'^invalid',invalid),
	url(r'^main_page/$',main_page),
    url(r'^logout/$',logout_page),
	# url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
	
	# url(r'^flashcard',flashcard),
    # url(r'^rank',rank),
	# Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
         #  url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
