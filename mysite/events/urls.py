from django.conf.urls import url

from . import views

app_name = 'events'

urlpatterns = [
	url(r'^(?P<page>[0-9]+)/page/$', views.page, name = 'page'),
	url(r'^categories/', views.CategoryView.as_view(), name  = 'redirect'),
	url(r'^category_results/', views.CategoryResultView.as_view(), name='category_results'),
]	
