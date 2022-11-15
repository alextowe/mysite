from django.contrib import admin
from .models import Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'list_order', 'date_added', 'url', 'is_published')
	list_display_links = ('id', 'title')
	search_field = ('title')
	list_per_page = 25

admin.site.register(Page, PageAdmin)
