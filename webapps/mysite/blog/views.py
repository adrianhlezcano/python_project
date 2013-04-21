# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import BlogPost

def index(request):
  post_list=BlogPost.objects.order_by('-timestamp')[:5]
  context={'post_list':post_list}
  return render(request, 'blog/index.html', context)
