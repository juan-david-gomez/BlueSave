from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BlueSave.views.home', name='home'),
     url(r'^', include('apps.Dinero.urls')),


    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
