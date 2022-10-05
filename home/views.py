from django.shortcuts import render
from . models import Category, Blog, Collection

# Create your views here.


def index(request):
    c = Collection.objects.all().order_by('-created')[0:5]
    blog = Blog.objects.all().order_by('-created')[0:6]
    context = {
        'c_list': c,
        'blog_list': blog,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'sobre.html')


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog_list': blog
    }
    return render(request, 'blog.html', context) 


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = {
        'blog_detail': blog, 
    }
    return render(request, 'detalhes-do-blog.html', context)


def contact(request):
    return render(request, 'contato.html')