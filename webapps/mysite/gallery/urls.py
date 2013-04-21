from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView

from gallery.models import Item, Photo

urlpatterns=patterns('',
  url(r'^$', 
    ListView.as_view(
      queryset=Item.objects.all()[:5],
      context_object_name='item_list',
      template_name='gallery/index.html'),
    name='index'),
  url(r'items/$',
    ListView.as_view(
      queryset=Item.objects.all(),
      context_object_name='item_list',
      template_name='gallery/item_list.html'),
    name='item_list'),
  url(r'^items/(?P<pk>\d+)/$',
    DetailView.as_view(
      model=Item,
      template_name='gallery/item.html'),
    name='item_detail'),
  url(r'^photos/(?P<pk>\d+)/$', 
    DetailView.as_view(
      model=Photo,
      template_name='gallery/photo_detail.html'),
    name='photo_detail'),
)
