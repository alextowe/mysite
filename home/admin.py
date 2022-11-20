from django.contrib import admin
from .models import Logo, Page

class LogoAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'logo_img', 'url', 'date_added', 'is_published')
	list_display_links = ('id', 'title')
	search_field = ('title')
	list_per_page = 25

admin.site.register(Logo, LogoAdmin)

class PageAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'list_order', 'url', 'date_added', 'is_published')
	list_display_links = ('id', 'title')
	search_field = ('title')
	list_per_page = 25

admin.site.register(Page, PageAdmin)
