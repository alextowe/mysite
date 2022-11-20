from django.db import models
from datetime import datetime

class Logo(models.Model):
	title = models.CharField(max_length=50)
	logo_img = models.ImageField(blank=True, upload_to='photos/logo/%Y/%m/%d/')
	url = models.CharField(max_length=50)
	date_added = models.DateTimeField(default=datetime.now, blank=True)
	is_published = models.BooleanField(default=False)
	def __str__(self):
		return self.title

class Page(models.Model):
	title = models.CharField(max_length=50)
	list_order = models.CharField(max_length=50)
	url = models.CharField(max_length=50)
	date_added = models.DateTimeField(default=datetime.now, blank=True)
	is_published = models.BooleanField(default=False)
	has_title = models.BooleanField(default=False)
	def __str__(self):
		return self.title
