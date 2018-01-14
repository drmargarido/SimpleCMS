#!/usr/bin/python
import sys
import os.path
import re
from django.core.management.base import BaseCommand, CommandError
from manager.models import Template

DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

class Command(BaseCommand):
	help = 'Register a new template in the easy_cms database'

	def add_arguments(self, parser):
		parser.add_argument("template_path", nargs="+", type=str)
		parser.add_argument('template_name', nargs='+', type=str)

	def handle(self, *args, **options):
		if options['template_path'] and options['template_name']:

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

			# Create template
			try:
				template = Template.objects.create(
					name=options["template_name"][0],
					file_path=options["template_path"][0]
				)
			except Exception:
				raise CommandError("Cannot create the template")

			# Register the template areas
			for area in areas:
				template.extendable_areas.create(name=area)

			template.save()
			self.stdout.write('Successfully created template "%s"' % template.name)
