from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.item_detail , name='item_detail'),
]
