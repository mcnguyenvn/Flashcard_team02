from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_flashcards.views.home', name='home'),
    # url(r'^django_flashcards/', include('django_flashcards.foo.urls')),
	url(r'^', include('Main_page.urls')),
	url(r'^', include('Registration.urls')),
	url(r'^flashcard/',include('flashcardapp.urls')),
    # url(r'^flashcard',flashcard),
    # url(r'^rank',rank),
	# Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
