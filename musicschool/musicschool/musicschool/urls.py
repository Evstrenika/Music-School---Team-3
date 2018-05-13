"""
Definition of urls for musicschool.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', musicschool.views.home, name='home'),
    # url(r'^musicschool/', include('musicschool.musicschool.urls')),

    ###
    #
    # domainname.com/instruments handled by instruments.url
    #
    ##
    #url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^instruments/', include('instruments.urls')), 
    url(r'^students/', include('students.urls')),
    url(r'^teachers/', include('teachers.urls')),
    url(r'^skills/', include('skills.urls')),
    url(r'^feedback/', include('feedback.urls')),
    url(r'^contracts/', include('contracts.urls')),
    url(r'^preferences/', include('preferences.urls')),
    url(r'^parents/', include('parents.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
