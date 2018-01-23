from django.contrib.auth.models import User
from django.db import models
from django.template.loader import render_to_string
import re
from simple_cms.settings import BASE_DIR

# Create your models here.

class Area(models.Model):
	name = models.CharField(max_length=50, null=False, blank=False)

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.template_set.all()[0].name + " -> " + self.name

	def as_json(self):
		return {
			"id": str(self.id),
			"name": self.name
		}

class Template(models.Model):
	name = models.CharField(max_length=150, unique=True)
	extendable_areas = models.ManyToManyField(Area)
	file_path = models.CharField(max_length=200)
	creation_date = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.name + " -> " + self.file_path

	def as_json(self):
		return {
			"id": str(self.id),
			"name": self.name,
			"path": self.file_path,
			"areas": [area.as_json() for area in self.extendable_areas.all()]
		}

class ArticleArea(models.Model):
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
	content = models.TextField()

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.article_set.all()[0].title + " -> " + self.area.name 

	def as_json(self):
		return {
			"id": str(self.id),
			"content": self.content,
			"area": self.area.as_json()
		}

DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

class Article(models.Model):
	template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True)
	content_areas = models.ManyToManyField(ArticleArea)
	title = models.CharField(max_length=150, blank=False, null=False)
	creation_date = models.DateTimeField(auto_now_add=True, editable=False)
	accesses_count = models.IntegerField(default=0)
	link = models.CharField(unique=True, max_length=200, blank=False)

	def get_article_page(self):
		article_html = ""
		template = render_to_string(BASE_DIR + "/" + self.template.file_path)
		for area in re.findall(DETECT_AREAS_REGEX, template):
			try:
				content_area = self.content_areas.get(area__name=area)
				template = template.replace(area, content_area.content)
			except Exception:
				print("Area not found -> " + area)
		
		template = template.replace("[[", "")
		template = template.replace("]]", "")

		return template

	def __str__(self):
		return self.__unicode__()

	def __unicode__(self):
		return self.template.name + " -> " + self.title

	def as_json(self):
		return {
			"id": str(self.id),
			"template": self.template.name,
			"content_areas": [area.as_json() for area in self.content_areas.all()],
			"title": self.title,
			"creation_date": str(self.creation_date),
			"accesses_count": str(self.accesses_count),
			"link": self.link
		}