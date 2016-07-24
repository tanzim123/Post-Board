from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.forms import ModelForm


# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft' , 'Draft'),
		('published' , 'Published'),
	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	#author = models.ForeignKey(User)
	body = models.TextField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(default=datetime.datetime.now)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	def __str__(self):
		return self.title


