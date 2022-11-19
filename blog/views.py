from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog(request):

	posts = Post.objects.order_by('date_added').filter(is_published=True)
	
	context = {
		'posts': posts,
	}
	
	return render(request, 'blog/blog.html', context)