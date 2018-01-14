#!/usr/bin/python
import sys
import os.path
import re
from django.core.management.base import BaseCommand, CommandError
from manager.models import Template, Article

DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

class Command(BaseCommand):
	help = 'Update the template areas'

	def add_arguments(self, parser):
		parser.add_argument('template_name', nargs='+', type=str)

	def handle(self, *args, **options):
		if options['template_name']:

			# Check if the received path is a file
			if not os.path.isfile(options['template_path'][0]):
				raise CommandError("File not found in the received path")

			# Check if the template name is not empty
			if len(options["template_name"][0]) == 0:
				raise CommandError("Empty template name received")				

			areas = []
			with open(options['template_path'][0], 'r') as template:
				# Find article areas in the template and register them along with the template
				for area in re.findall(DETECT_AREAS_REGEX, template.read()):
					areas.append(area)

			# Get template
			try:
				template = Template.objects.get(name=options["template_name"][0])
			except Exception:
				raise CommandError("Cannot create the template")

			template_areas = [area.name for area in template.extendable_areas.all()]

			template_articles = Article.objects.filter(template=template)
			
			# Register new areas in the html template areas
			for area in areas:
				if area not in template_areas:
					new_area = template.extendable_areas.create(name=area)
					self.stdout.write('Added area "%s"' % new_area.name)		

					# Register new area in the template articles
					for article in template_articles:
						content_areas.create(area=new_area, content="")

			template.save()
			self.stdout.write('Successfully updated template "%s"' % template.name)
