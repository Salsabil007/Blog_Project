from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BlogForm
from .models import Blog


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            #return redirect('/blog/' + str(blog_item.id) + '/')
            return redirect('/polls/')
    else:
        form = BlogForm()
    return render(request, 'polls/blog_form.html', {'form': form})