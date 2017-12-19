from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.forms import BlogForm, ContentForm
from django.http import HttpResponse

from .models import Blog_Table
from django.template import loader


def index2(request):
    latest_question_list = Blog_Table.objects.all()
    template = loader.get_template('blog/index2.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    return HttpResponse("Hello, world. You're at the blog project")


def add_bloginfo(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save()
            blog_item.save()
            #return redirect('/blog/' + str(blog_item.id) + '/')
            return redirect('/blog/')
    else:
        form = BlogForm()
    return render(request, 'blog/blog.html', {'form': form})


def add_content(request):
    if request.method == "POST":
        form = ContentForm(request.POST)
        if form.is_valid():
            blog_item = form.save()
            blog_item.save()
            #return redirect('/blog/' + str(blog_item.id) + '/')
            return redirect('/blog/')
    else:
        form = ContentForm()
    return render(request, 'blog/content.html', {'form': form})