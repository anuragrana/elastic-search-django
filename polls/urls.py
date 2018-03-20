from django.conf.urls import url
from . import views

app_name='polls'

urlpatterns = [
    url(r'^search/$', views.search, name='api_search'),
    url(r'^searchbook/$', views.searchbook, name='api_search_book'),
    url(r'^searchproduct/$', views.searchproduct, name='api_search_product'),
    url(r'^signinpage/$', views.opensigninpage, name='signinpage'),
    url(r'^signuppage/$', views.opensignuppage, name='signuppage'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signout/$', views.signout, name='signout'),
]