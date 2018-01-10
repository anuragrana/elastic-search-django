from django.conf.urls import url
from . import views

app_name='polls'

urlpatterns = [
    url(r'^search/$', views.search, name='api_search'),
    url(r'^searchbook/$', views.searchbook, name='api_search_book'),
    url(r'^searchbook/$', views.searchproduct, name='api_search_product'),
]