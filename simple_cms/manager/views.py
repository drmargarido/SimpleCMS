from django.shortcuts import render

# Create your views here.

def initial_page(request):
	return render(request, "templates/index.html", {})

def article_page(request, article_id):
	return render()