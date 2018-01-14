from django.urls import path
from manager.views import article_page

urlpatterns = [
	path("<int:article_id>/", article_page),
]