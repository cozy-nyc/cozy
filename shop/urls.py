from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w\d]+)/$', views.item_detail , name='item_detail'),
    url(r'^s/(?P<item_id>\d+)/(?P<item_slug>[-\w]+)/(?P<id>\d+)/$', views.listing , name='listing'),
    url(r'^sell/$', views.post_listing, name='sell'),
    url(r'^api/$', views.ItemList.as_view()),
 	url(r'^api/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

]
