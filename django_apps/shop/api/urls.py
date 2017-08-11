from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns




urlpatterns = [

    url(r'^api/category/$', views.CategoryList.as_view()),
 	url(r'^api/category/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^api/subCategory/$', views.SubCategoryList.as_view()),
    url(r'^api/subCategory/create$', views.SubCategoryCreate.as_view()),
 	url(r'^api/subCategory/(?P<pk>[0-9]+)/$', views.SubCategoryDetial.as_view()),
    url(r'^api/listing/create/$', views.ListingCreate.as_view()),
    url(r'^api/listings/edit/(?P<pk>[0-9]+)/$', views.ListingUpdate.as_view()),
    url(r'^api/listings/delte/(?P<pk>[0-9]+)/$', views.ListingDelete.as_view()),
    url(r'^api/listings/(?P<pk>[0-9]+)/$', views.ListingDetial.as_view()),
    url(r'^api/listings/$', views.ListingList.as_view()),
    url(r'^api/transaction/$', views.TransactionList.as_view()),
 	url(r'^api/transaction/(?P<pk>[0-9]+)/$', views.TransactionDetail.as_view()),
    url(r'^api/items/$', views.ItemList.as_view()),
    url(r'^api/items/create/$', views.ItemCreate.as_view()),
 	url(r'^api/items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^api/items/edit/(?P<pk>[0-9]+)/$', views.ItemUpdate.as_view()),
    url(r'^api/items/delete/(?P<pk>[0-9]+)/$', views.ItemDelete.as_view()),

]
