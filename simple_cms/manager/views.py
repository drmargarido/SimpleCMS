from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from manager.models import Article, Template, ArticleArea
from manager.forms import NewTemplateForm, NewArticleForm
import re


def index_page(request):
	return render(request, "manager/index.html", {"article_list": Article.objects.all()})


def dashboard_page(request):
	return render(request, "manager/dashboard.html", {
		"NewTemplateForm": NewTemplateForm(),
		"NewArticleForm": NewArticleForm(),
		"templates": Template.objects.filter(is_active=True),
		"articles": Article.objects.all()
	})


def edit_article_page(request, article_id):
	return render(request, "manager/article.html", {})


def article_page(request, article_id):
	try:
		article = Article.objects.get(id=int(article_id))
	except Exception:
		return HttpResponse(status=400, content="400 Article not found")

	return HttpResponse(article.get_article_page())


def article_page_by_link(request, link):
	try:
		article = Article.objects.get(link=link)
	except Exception:
		return HttpResponse(status=400, content="400 Article not found")

	return HttpResponse(article.get_article_page())


DETECT_AREAS_REGEX = re.compile("\[\[\s*([0-9a-zA-Z_\-]+)\s*\]\]", re.DOTALL)

def add_template(request):
	if not request.method == 'POST':
		return HttpResponse(status=400)

	new_template_form = NewTemplateForm(request.POST)
	if not new_template_form.is_valid():
		return HttpResponse(status=400, content="Invalid data received")
	
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

def deactivate_template(request):
	template_id = request.POST.get("template_id", "")
	
	if template_id == "":
		return HttpResponse(status=400, content="Missing mandatory template_id")

	template = Template.objects.get(id=template_id)
	if not template.is_active:
		return HttpResponse(status=400, content="The received template is not active")

	template.is_active = False
	template.save()

	return HttpResponse(status=200)


def add_article(request):
	if not request.method == 'POST':
		return HttpResponse(status=400)

	new_article_form = NewArticleForm(request.POST)
	print(new_article_form)
	if not new_article_form.is_valid():
		return HttpResponse(status=400, content="Invalid data received")

	try:
		template = Template.objects.get(id=new_article_form["template"].data)
	except Exception:
		return HttpResponse(status=400, content="The received template does not exist")

	if not template.is_active:
		return HttpResponse(status=400, content="Selected template is disabled")

	article = Article.objects.create(
		template = template,
		title = new_article_form["title"].data,
		link = new_article_form["link"].data
	)

	for area in template.extendable_areas.all():
		article.content_areas.create(
			area = area,
			content = ""
		)

	article.save()
	return redirect('/article/' + str(article.id) + '/')


def delete_article(request):
	article_id = request.POST.get("article_id", "")

	if article_id == "":
		return HttpResponse(status=400, content="Missing mandatory data")

	try:
		article = Article.objects.get(id=article_id)
	except Exception:
		return HttpResponse(status=400, content="The received article does not exist")

	for area in article.content_areas.all():
		area.delete()

	article.delete()

	return HttpResponse(status=200)


def edit_article_page(request, article_id):
	try:
		article = Article.objects.get(id=article_id)
	except Exception:
		return HttpResponse(status=400, content="The received article does not exist")

	return render(request, "manager/article.html", {"article": article})


def save_content(request):
	content_area_id = request.POST.get("content_area_id", "")
	content = request.POST.get("content", "")

	if content_area_id == "":
		return HttpResponse(status=400, content="Missing mandatory data")

	try:
		content_area = ArticleArea.objects.get(id=content_area_id)
	except Exception:
		return HttpResponse(status=400, content="The received article area does not exist")

	content_area.content = content
	content_area.save()
	return HttpResponse(status=200)
