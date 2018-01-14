#!/usr/bin/python
import sys
import os.path
import re
from django.core.management.base import BaseCommand, CommandError
from manager.models import Article, Template

class Command(BaseCommand):
	help = 'Remove a article from the easy_cms database'

	def add_arguments(self, parser):
		parser.add_argument("article_id", nargs="+", type=str)

	def handle(self, *args, **options):
		if options['article_id']:

			# Remove article
			try:
				article = Article.objects.get(options["article_id"][0])
				article_title = article.title

				for area in article.content_areas.all():
					area.delete()

				article.delete()

			except Exception:
				raise CommandError("Cannot remove the article")

			self.stdout.write('Successfully removed the article "%s"' % article_title)
