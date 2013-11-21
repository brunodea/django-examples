from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

def search_form(request):
	return render(request, 'search_form.html')

def search(request):
	error = False
	page = 'search_form.html'
	context = {}
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			error = True
		else:
			books = Book.objects.filter(title__icontains=q) #case insensitive
			context = {'books': books, 'query': q}
			page = 'search_results.html'
	context['error'] = error
	return render(request, page, context)
