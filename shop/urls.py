from django.conf.urls import url
from . import views
from profiles.views import (login_view, signup_view, logout_view)

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail , name='product_detail'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^signup/', signup_view, name='signup'),


]
