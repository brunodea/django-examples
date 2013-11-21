from django.shortcuts import render
from django.http import HttpResponse

from books.models import Book

def search_form(request):
	return render(request, 'search_form.html')

def search(request):
	context = {'error': True}
	page = 'search_form.html'
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		books = Book.objects.filter(title__icontains=q) #case insensitive
		context = {'books': books, 'query': q}
		page = 'search_results.html'
	return render(request, page, context)
