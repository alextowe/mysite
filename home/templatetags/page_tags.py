from django import template
from home.models import Logo, Page

register = template.Library()

@register.inclusion_tag('partials/_navbar.html')
def render_nav_menu():
	"""Renders the logo and pages models to the navbar."""
	logo = Logo.objects.filter(is_published=True)
	pages = Page.objects.order_by('list_order').filter(is_published=True)
	nav_items = {'logo':logo, 'pages':pages}
	return nav_items
	
@register.inclusion_tag('partials/_titlebar.html')
def render_title_bar(path):
	"""Renders the title bar for all pages except home."""
	if path == '/':
		return None
	else:
		pages = Page.objects.order_by('list_order').filter(is_published=True).exclude(url='index')
		path = path[1:][:-1]
		for page in pages:
			if page.url == path:
				current_page = page
				
		context = {'page':current_page}
		return context