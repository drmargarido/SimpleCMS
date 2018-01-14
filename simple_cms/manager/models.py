from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string

# Create your models here.

class Area(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.template_set.all()[0].name + " -> " + self.name

class Template(models.Model):
	name = models.CharField(max_length=150, unique=True)
	extendable_areas = models.ManyToManyField(Area)
	file_path = models.CharField(max_length=200)
	creation_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.name + " -> " + self.file_path 

class ArticleArea(models.Model):
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
	content = models.TextField()

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.article_set.all()[0].title + " -> " + self.area.name 


DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

class Article(models.Model):
	template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
	content_areas = models.ManyToManyField(ArticleArea)
	title = models.CharField(max_length=150, blank=False, null=False)
	creation_date = models.DateTimeField(auto_now_add=True, editable=False)
	accesses_count = models.IntegerField(default=0)
	link = models.CharField(unique=True, max_length=300, blank=False)

	def get_article_page(self):
		article_html = ""
		template = render_to_string(self.template.file_path)

		return template

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.template.name + " -> " + self.title