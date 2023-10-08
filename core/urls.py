from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('projects/', views.ProjectView.as_view(), name='projects')
]


