from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index'),
    url(r'^all_events/', views.all_events, name='all_events'),
    url(r'^delete', views.delete, name='delete'),
    url(r'^create', views.create, name='create')
]
