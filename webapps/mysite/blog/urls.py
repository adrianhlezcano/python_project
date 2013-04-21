from django.conf.urls import patterns, url
from django.utils import timezone

from blog import views
from blog.models import BlogPost

urlpatterns=patterns('', 
  # http://localhost:8000/blog
  url(r'^$', views.index, name='index'),

)
