from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Logo, Page
from pages.views import navbar

def blog(request):
	logo, pages = navbar(Logo, Page)
	
	context = {
		'logo': logo,
		'pages': pages,
	}
	
	return render(request, 'blog/blog.html', context)