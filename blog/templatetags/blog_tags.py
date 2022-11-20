from django import template
from blog.models import Post
register = template.Library()
	
@register.inclusion_tag('blog/cards.html')
def render_cards():
	"""Renders blog posts in order of newest to oldest."""
	posts = Post.objects.order_by('-date_added').filter(is_published=True)
	return {'posts':posts}
	
@register.inclusion_tag('blog/post.html')
def render_post():
	"""Renders blog posts in order of newest to oldest."""
	posts = Post.objects.order_by('-date_added').filter(is_published=True)
	return {'posts':posts}