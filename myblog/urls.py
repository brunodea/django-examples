from django.conf.urls import patterns, include, url
from myblog.views import hello, curr_datetime, hours_ahead, conditional_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/$', include(admin.site.urls)),
	url(r'^hello/$', hello),
	url(r'^time/$', curr_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead), #regex que limita em numero de 1 a 2 digitos. \d+ eh para qualquer numero
	#cuidar espaco depois da virgula nos regex.
	url(r'^time/plus/conditional/(\d{1,2})/$', conditional_datetime)
)
