from django.urls import path
from manager.views import index_page, article_page, article_page_by_link, dashboard_page

urlpatterns = [
	path("", index_page),
	path("<int:article_id>/", article_page),
	path("dashboard/", dashboard_page),
	path("<str:link>/", article_page_by_link),
]