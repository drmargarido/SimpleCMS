from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from manager.models import Article, Template
from manager.forms import NewTemplateForm
import re


def index_page(request):
	return render(request, "manager/index.html", {"article_list": Article.objects.all()})


def dashboard_page(request):
	return render(request, "manager/dashboard.html", {
		"NewTemplateForm": NewTemplateForm(),
		"templates": Template.objects.all()
	})


def edit_article_page(request, article_id):
	return render(request, "manager/article.html", {})


def article_page(request, article_id):
	try:
		article = Article.objects.get(id=int(article_id))
	except Exception:
		return HttpResponse(status=404, content="404 Article not found")

	return HttpResponse(article.get_article_page())


def article_page_by_link(request, link):
	try:
		article = Article.objects.get(link=link)
	except Exception:
		return HttpResponse(status=404, content="404 Article not found")

	return HttpResponse(article.get_article_page())


DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

def add_template(request):
	if not request.method == 'POST':
		return HttpResponse(status=404)

	new_template_form = NewTemplateForm(request.POST)
	if not new_template_form.is_valid():
		return HttpResponse(status=400)
	
	# Create template	
	template = Template.objects.create(
		name=new_template_form["name"].data,
		file_path=new_template_form["path"].data
	)

	with open(template.file_path, 'r') as template_file:
		# Find article areas in the template and register them along with the template
		for area in re.findall(DETECT_AREAS_REGEX, template_file.read()):
			template.extendable_areas.create(name=area)

	template.save()
	return redirect('/dashboard/')

	