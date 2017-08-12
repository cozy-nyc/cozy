from django.conf.urls import url,include
from . import views
from .api import views as api_views



urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w\d]+)/$', views.item_detail , name='item_detail'),
    url(r'^s/(?P<item_id>\d+)/(?P<item_slug>[-\w]+)/(?P<id>\d+)/$', views.listing , name='listing'),
    url(r'^sell/$', views.post_listing, name='sell'),
    url(r'^', include('django_apps.shop.api.urls',namespace = 'shopAPI'))

]
