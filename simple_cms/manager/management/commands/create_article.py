#!/usr/bin/python
import sys
import os.path
import re
from django.core.management.base import BaseCommand, CommandError
from manager.models import Article, Template

class Command(BaseCommand):
	help = 'Register a new article in the easy_cms database'

	def add_arguments(self, parser):
		parser.add_argument("template_name", nargs="+", type=str)
		parser.add_argument("article_title", nargs="+", type=str)
		parser.add_argument('article_link', nargs='+', type=str)

	def handle(self, *args, **options):
		if options['template_name'] and options["article_title"]:
			if options["article_link"]:
				article_link = options["article_link"][0]
			else:
				article_link = ""

			# Create article
			try:
				template = Template.objects.get(name=options["template_name"][0])
				article = Article.objects.create(
					template = template,
					title = options["article_title"][0],
					link = article_link
				)

				for area in template.extendable_areas.all():
					article.content_areas.create(
						area = area,
						content = ""
					)

				article.save()

			except Exception:
				raise CommandError("Cannot create the template")

			self.stdout.write('Successfully created article "%s"' % article.title)
