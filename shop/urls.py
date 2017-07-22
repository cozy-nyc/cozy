from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^s/(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
    url(r'^s/(?P<id>\d+)/(?P<slug>[-\w\d]+)/$', views.item_detail , name='item_detail'),
    url(r'^s/(?P<item_id>\d+)/(?P<item_slug>[-\w]+)/(?P<id>\d+)/$', views.listing , name='listing'),
    url(r'^sell/$', views.post_listing, name='sell'),
    url(r'^api/category/$', views.CategoryList.as_view()),
 	url(r'^api/category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^api/subCategory/$', views.SubCategoryList.as_view()),
 	url(r'^api/subCategory/(?P<pk>[0-9]+)/$', views.SubCategoryDetial.as_view()),
    url(r'^api/listing/$', views.ListingList.as_view()),
 	url(r'^api/listing/(?P<pk>[0-9]+)/$', views.ListingDetial.as_view()),
    url(r'^api/transaction/$', views.TransactionList.as_view()),
 	url(r'^api/transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^api/items/$', views.ItemList.as_view()),
 	url(r'^api/items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

]
