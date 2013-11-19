from django.conf.urls import patterns, include, url
from myblog.views import curr_datetime, hours_ahead

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/$', include(admin.site.urls)),
	url(r'^$', curr_datetime),
	url(r'^time/$', curr_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
)
