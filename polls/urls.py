from django.conf.urls import url
from . import views

app_name='polls'

urlpatterns = [
    url(r'^search/$', views.search, name='api_search'),
    
]