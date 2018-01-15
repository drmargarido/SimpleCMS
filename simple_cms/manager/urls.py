from django.urls import path
from manager.views import article_page, article_page_by_link

urlpatterns = [
	path("<int:article_id>/", article_page),
	path("<str:link>/", article_page_by_link),
]