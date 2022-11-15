from django.shortcuts import render
from .models import Logo, Page
from django.http import HttpResponse

def navbar(Logo, Page):
	logo = Logo.objects.filter(is_published=True)
	pages = Page.objects.order_by('list_order').filter(is_published=True)

	return logo, pages
	
def index(request):
	logo, pages = navbar(Logo, Page)
	
	context = {
		'logo': logo,
		'pages': pages,
	}
	
	return render(request, 'pages/index.html', context)

def about(request):
	logo, pages = navbar(Logo, Page)
	
	context = {
		'logo': logo,
		'pages': pages,
	}

	return render(request, 'pages/about.html', context)