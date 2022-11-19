from django import template
from blog.models import Post
register = template.Library()

@register.inclusion_tag('blog/card.html')
def render_cards():
	"""Renders blog posts in order of newest to oldest."""
	posts = Post.objects.order_by('-date_added').filter(is_published=True)
	context = {'posts':posts}
	return context

@register.inclusion_tag('blog/card.html')
def render_post(slug):
	"""Renders post from slug."""
	posts = Post.objects.filter(is_published=True)
	for post in posts:
		if post.slug == slug:
			current_post = post
	context = {'post':current_post,}
	return context