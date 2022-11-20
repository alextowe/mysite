from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def blog(request):
	posts = Post.objects.filter(is_published=True)
	context = {
		'posts': posts,
	}	
	return render(request, 'blog/blog.html', context)
	
def post_detail(request, slug):
	posts = Post.objects.filter(is_published=True)
	for post in posts:
		if post.slug == slug:
			current_post = post
	context = {
		'post': current_post,
	}
	return render(request, 'blog/post.html', context)
