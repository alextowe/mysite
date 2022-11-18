from django.shortcuts import render
from .models import Logo, Page
from django.http import HttpResponse
	
def index(request):
	
	context = {
	}
	
	return render(request, 'pages/index.html', context)

def about(request):
	
	context = {
		
	}

	return render(request, 'pages/about.html', context)