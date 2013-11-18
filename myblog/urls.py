from django.conf.urls import patterns, include, url
from myblog.views import hello, curr_datetime, hours_ahead, personal_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/$', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^time/$', curr_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead), #regex que limita em numero de 1 a 2 digitos. \d+ eh para qualquer numero
	url(r'^time/personal/$', personal_datetime)
)
