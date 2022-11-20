from django import template
from home.models import Logo, Page
from blog.models import Post

register = template.Library()

@register.inclusion_tag('partials/_navbar.html')
def render_nav_menu():
	"""Renders the logo and pages models to the navbar."""
	logo = Logo.objects.filter(is_published=True)
	pages = Page.objects.order_by('list_order').filter(is_published=True)
	return {'logo':logo, 'pages':pages}
	
@register.inclusion_tag('partials/_titlebar.html')
def render_title_bar(path):
	"""Renders the title bar for all pages except home. Subsitutes post title for page title on post detail page."""
	if path == '/':
		return None
	elif len(path.split('/')) <= 3:
		path = path.split('/')[1]
		context = Page.objects.filter(is_published=True, has_title=True, url=path).exclude(url='index')[0]
	elif len(path.split('/')) > 3:
		path = path.split('/')[2]
		context = Post.objects.filter(is_published=True, has_title=True, slug=path)[0]
	
	return {'context':context}
				
				