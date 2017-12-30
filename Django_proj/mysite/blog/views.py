from django.http import HttpResponse
from django.shortcuts import redirect, render

from blog.forms import BlogForm, ContentForm
from django.http import HttpResponse

from .models import Blog_Table,Blog_Part
from django.template import loader
from django.shortcuts import get_object_or_404


def index2(request):
    latest_question_list = Blog_Table.objects.all()
    template = loader.get_template('blog/index2.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def get_content(request, table_id, part_id):
    #content=Blog_Part.objects.filter(id=part_id,blogID=table_id)
    #template = loader.get_template('blog/contentofblog.html')
    #context = {
    #    'content': content,
    #}
    #return HttpResponse(template.render(context, request))
    content = get_object_or_404(Blog_Part, pk=part_id,blogID=table_id)
    return render(request, 'blog/contentofblog.html', {'content': content})


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
            blog_item.blogID = a

            blog_item.save()

            #return redirect('/blog/' + str(blog_item.id) + '/')
            return redirect('/blog/')
    else:
        form = ContentForm()
    return render(request, 'blog/content.html', {'form': form})

def update_blog(request, table_id, part_id):
    instance=Blog_Part.objects.get(pk=part_id,blogID=table_id)
    if request.method == "POST":
        form= ContentForm(request.POST, instance=instance)
        if form.is_valid():
            editedentry= form.save()
            editedentry.save()
            return redirect('/blog/')

    else:
        form= ContentForm(instance=instance)

        return render(request, 'blog/content.html', {'form': form})