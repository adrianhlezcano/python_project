from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.utils import timezone

from polls import views
from polls.models import Poll, Choice

urlpatterns=patterns('',
  # http://localhost/polls/
  #url(r'^$', views.index, name='index'),
  # /polls/5
  #url(r'(?P<poll_id>\d+)/$', views.detail, name='detail'),
  # /polls/3/results
  #url(r'(?P<poll_id>\d+)/results/$', views.results, name='results'),
  # /polls/3/vote
  #url(r'(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
  ### REFACTORING ###
  url(r'^$', 
    ListView.as_view(
      #queryset=Poll.objects.order_by('-pub_date')[:5],
      queryset=Poll.objects.filter(pub_date__lte=timezone.now)\
        .order_by('-pub_date')[:5],
      context_object_name='poll_list',
      template_name='polls/index.html'),
    name='index'),
  url(r'^(?P<pk>\d+)/$',
    DetailView.as_view(
      queryset=Poll.objects.filter(pub_date__lte=timezone.now),
      model=Poll,
      template_name='polls/details.html'),
    name='detail'),
  url(r'^(?P<pk>\d+)/results/$',
    DetailView.as_view(
      model=Poll,
      template_name='polls/results.html'),
    name='results'),
  url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote', name='vote'),
)
