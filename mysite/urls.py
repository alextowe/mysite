"""mysite URL Configuration

"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('pages.urls')),
	path('blog', include('blog.urls')),
	path('admin/', admin.site.urls),
]
