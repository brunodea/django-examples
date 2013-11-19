from django.http import HttpResponse
from datetime import datetime, timedelta
from django.template import Template, Context
from django.template.loader import get_template

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

def conditional_datetime(request, plus):
	
	invalid = False
	try:
		plus = int(plus)
	except ValueError:
		invalid = True
		plus = 0

	invalid = plus > 24

	t = get_template("home.html")
	c = Context({"server_name" : "GlaDUS", "time" : datetime.now() + timedelta(hours = plus), "invalid_plus": invalid})

	return HttpResponse(t.render(c))

