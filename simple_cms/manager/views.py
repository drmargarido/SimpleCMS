from django.shortcuts import render
from django.http import HttpResponse
from manager.models import Article

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