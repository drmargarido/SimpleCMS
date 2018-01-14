from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Area(models.Model):
	name = models.CharField(null=False, blank=False)

class Template(models.Model):
	name = models.CharField(unique=True)
	extendable_areas = models.ManyToManyField(Area)
	file_path = models.CharField()
	creation_date = models.DateTimeField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.SET_NULL)

class ArticleArea(models.Model):
	area = models.ForeignKey(Area, on_delete=models.SET_NULL)
	content = models.TextField()

class Article(models.Model):
	author = models.ForeignKey(User, on_delete=models.SET_NULL)
	template = models.ManyToManyField(ArticleArea, on_delete=models.SET_NULL)
	title = models.CharField(max_length=150, blank=False, null=False)
	creation_date = models.DateTimeField(auto_now_add=True, editable=False)
	accesses_count = models.IntegerField(default=0)
	link = models.CharField(max_length=150, blank=False)
