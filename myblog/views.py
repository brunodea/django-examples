from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Template, Context

def hello(request):
	return HttpResponse("Hello World")

#hora depende da time-zone.
def curr_datetime(request):
	now = datetime.now()
	html = "<html><body>It is %s.</body></html>" % now
	return HttpResponse(html)

def hours_ahead(request, plus):
	try:
		plus = int(plus)
	except ValueError:
		raise Http404()
	ahead = datetime.now() + timedelta(hours = plus)
	html = "<html><body>In %d hour(s), it will be %s.</body></html>" % (plus, ahead)
	return HttpResponse(html)

def personal_datetime(request):
	raw_template = "<html><body> Hello, my name is {{ server_name }} and it is {{ time }}.</html></body>"

	t = Template(raw_template)
	c = Context({"server_name" : "GlaDUS", "time" : datetime.now()})

	return HttpResponse(t.render(c))

