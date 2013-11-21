from django.conf.urls import patterns, include, url
from myblog.views import curr_datetime, hours_ahead
from books.views import search_form, search
from contact.views import contact, contact_thanks

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/$', search),
	url(r'^time/$', curr_datetime),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^contact/$', contact),
	url(r'^contact/thanks/$', contact_thanks),
	url(r'^$', curr_datetime),
)
