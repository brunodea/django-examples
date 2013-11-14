from django.http import HttpResponse
from datetime import datetime

def hello(request):
	return HttpResponse("Hello World")

def curr_datetime(request):
	now = datetime.now()
	html = "<html><body>It is %s.</body></html>" % now
	return HttpResponse(html)
