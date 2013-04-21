# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

import datetime
from polls.models import Poll, Choice


def index(request):
  response = HttpResponse()
  expire=datetime.datetime.today() + datetime.timedelta(days=1)
  name=request.COOKIES.get('name')
  if not name:
    response.set_cookie('name', 'Adrian', expires=expire)
    response.write("Hello World. You're at the poll index from %s\n" % request.get_host())
  else:
    response.write("You're %s from %s\n" % (name, request.get_host()))
  poll_list=Poll.objects.order_by('-pub_date')[:5]
  #template=loader.get_template('polls/index.html')
  #context=Context({
  #  'poll_list':poll_list,
  #})
  #response.write(template.render(context))
  context={ 'poll_list':poll_list }
  return render(request, 'polls/index.html', context)

def detail(request, poll_id):
  #try:
  #  poll=Poll.objects.get(id=poll_id)
  #except:
  #  raise Http404
  #return render(request, 'polls/details.html', {'poll' : poll })
  poll=get_object_or_404(Poll, pk=poll_id)
  return render(request, 'polls/details.html', {'poll': poll})

def results(request, poll_id):
  poll=get_object_or_404(Poll, pk=poll_id)
  return render(request, 'polls/results.html', {'poll': poll})


def vote(request, poll_id):
 poll=get_object_or_404(Poll, pk=poll_id)
 try:
   selected_choice=poll.choice_set.get(pk=request.POST['choice'])
 except (KeyError, Choice.DoesNotExist):
   return render(request, 'polls/details.html',\
     {'poll':poll, 'error_message': 'You didn\'t selected any choice'})
 else:
   selected_choice.votes += 1
   selected_choice.save()
   return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
