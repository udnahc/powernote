# Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response
from blog.models import PowerNoteBlog
from django.http import HttpResponse

def index(request):
    latest_blog_list = PowerNoteBlog.objects.all()
    t = loader.get_template('blogs/index.html')
    c = Context({
        'latest_blog_list': latest_blog_list,
    })
    return HttpResponse(t.render(c))

def detail(request, blog_id):
    latest_blog_list = PowerNoteBlog.objects.get(pk=blog_id)
    t = loader.get_template('blogs/details.html')
    c = Context({
        'latest_blog_list': latest_blog_list,
    })
    return HttpResponse(t.render(c))

# def index(request):
#     latest_blog_list = PowerNoteBlog.objects.all().order_by('-pub_date')[:5]
#     op = ', '.join([q.author for q in latest_blog_list])
#     return HttpResponse(op)
