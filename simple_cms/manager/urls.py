from django.urls import path
from manager.views import initial_page

urlpatterns = [
	path("index/", initial_page)
]