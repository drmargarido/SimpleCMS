from django.shortcuts import render

# Create your views here.

def initial_page(request):
	return render(request, "templates/index.html", {})

def article_page(request, article_id):
	try:
		article = Article.objects.get(article_id)
	except Exception:
		return render(request, "", {})

	return render()