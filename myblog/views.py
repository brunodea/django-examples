from datetime import datetime, timedelta
from django.shortcuts import render

#hora depende da time-zone.
def curr_datetime(request):
	now = datetime.now()
	return render(request, 'home.html', {'time':now})

def hours_ahead(request, plus):
	try:
		plus = int(plus)
	except ValueError:
		raise Http404()
	ahead = datetime.now() + timedelta(hours = plus)
	return render(request, 'future.html', {'hour_offset':plus, 'next_time':ahead})



