from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'author', 'author_img', 'date_added', 'is_published')
	list_display_links = ('id', 'title')
	search_field = ('title')
	list_per_page = 25

admin.site.register(Post, PostAdmin)