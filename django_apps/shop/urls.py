from django.conf.urls import url,include
from . import views
from .api import views as api_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w\d]+)/$', TemplateView.as_view(template_name="index.html")),
    url(r'^s/(?P<item_id>\d+)/(?P<item_slug>[-\w]+)/(?P<id>\d+)/$', TemplateView.as_view(template_name="index.html")),
    url(r'^sell/$', views.post_listing, name='sell'),
    url(r'^', include('django_apps.shop.api.urls',namespace = 'shopAPI'))
\
]
