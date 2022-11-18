from django import template
from pages.models import Logo, Page
register = template.Library()

@register.inclusion_tag('partials/_navbar.html')
def render_nav_menu():
	"""Renders the logo and pages models to the navbar."""
	
	logo = Logo.objects.filter(is_published=True)
	pages = Page.objects.order_by('list_order').filter(is_published=True)
	nav_items = {'logo':logo, 'pages':pages}
	return nav_items