from django.conf.urls import url

from search import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^search$', views.search),
    url(r'^suggest$', views.suggest, name='suggest'),
]