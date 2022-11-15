from django.shortcuts import render
from .models import Page
from django.http import HttpResponse

def index(request):
	pages = Page.objects.order_by('list_order').filter(is_published=True)
	
	context = {
		'pages': pages,
	}

	return render(request, 'pages/index.html', context)

def about(request):
	pages = Page.objects.order_by('list_order').filter(is_published=True)
	
	context = {
		'pages': pages,
	}

	return render(request, 'pages/about.html', context)