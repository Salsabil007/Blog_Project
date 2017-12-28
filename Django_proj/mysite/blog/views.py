from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.forms import BlogForm, ContentForm
from django.http import HttpResponse

from .models import Blog_Table
from django.template import loader
from django.shortcuts import get_object_or_404


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


def add_content(request, aaa_id):
    if request.method == "POST":
        a = get_object_or_404(Blog_Table, id=aaa_id)
        form = ContentForm(request.POST)
        if form.is_valid():
            #form.userID=a.id
            blog_item = form.save(commit=False)
            blog_item.userID = a

            blog_item.save()

            #return redirect('/blog/' + str(blog_item.id) + '/')
            return redirect('/blog/')
    else:
        form = ContentForm()
    return render(request, 'blog/content.html', {'form': form})