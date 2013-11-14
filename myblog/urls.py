from django.conf.urls import patterns, include, url
from myblog.views import hello, curr_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/$', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^time/$', curr_datetime)  
)
