#from django.shortcuts import render


# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from MyBlog.models import BlogPost
import html

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
#   c = Context({'posts': posts})
    h = t.render({'posts': posts})
    return HttpResponse(h)
#   return HttpResponse(t.render(c))´íÎóµÄ