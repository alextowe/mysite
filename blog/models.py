from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=50)
	author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
	author_img = models.ImageField(blank=True, upload_to='photos/logo/%Y/%m/%d/')
	content = models.TextField(blank=True)
	date_added = models.DateTimeField(auto_now= True)
	is_published = models.BooleanField(default=False)
	
	def __str__(self):
		return self.title
