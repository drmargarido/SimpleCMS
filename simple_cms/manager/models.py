from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Area(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)

class Template(models.Model):
	name = models.CharField(max_length=150, unique=True)
	extendable_areas = models.ManyToManyField(Area)
	file_path = models.CharField(max_length=200)
	creation_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class ArticleArea(models.Model):
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
	content = models.TextField()

class Article(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	template = models.ManyToManyField(ArticleArea)
	title = models.CharField(max_length=150, blank=False, null=False)
	creation_date = models.DateTimeField(auto_now_add=True, editable=False)
	accesses_count = models.IntegerField(default=0)
	link = models.CharField(max_length=150, blank=False)
