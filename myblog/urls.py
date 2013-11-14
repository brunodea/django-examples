from django.conf.urls import patterns, include, url
from myblog.views import hello

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^hello/$', hello)
)
