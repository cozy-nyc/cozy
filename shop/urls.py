from django.conf.urls import url
from . import views
from profiles.views import (login_view, signup_view, logout_view, ProfileView )

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.item_detail , name='item_detail'),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^signup/', signup_view, name='signup'),
    url(r'^(?P<username>[\w.@+-]+)/$', ProfileView.as_view(), name='detail'), # /tweet/1/



]
