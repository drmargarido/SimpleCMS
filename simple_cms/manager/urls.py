from django.urls import path
from manager.views import index_page, article_page, article_page_by_link, dashboard_page, add_template, deactivate_template, add_article

urlpatterns = [
	path("", index_page),
	path("dashboard/", dashboard_page),
	path("add_template/", add_template),
	path("deactivate_template/", deactivate_template),
	path("add_article/", add_article),
	path("<int:article_id>/", article_page),
	path("<str:link>/", article_page_by_link),
]