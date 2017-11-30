from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.forms import ModelForm
from django.views.generic import TemplateView

from blog.forms import AuthorForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Author



class HomeView(TemplateView):
    template_name = 'blog/blog_page.html'


    def post(self, request, text=None):
        form = AuthorForm(request.POST)
        if form.is_valid():
         #   name = form.save(commit=False)
            form.save(commit=False)

            text = form.cleaned_data['post']
            form = AuthorForm()
            return redirect('home:vote')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)





def addbook(request):
    form = AuthorForm()


    if request.POST:
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            form=AuthorForm()

            return redirect('blog/vote')
          #  book_formset = BookFormset(request.POST, instance=author)
           # if book_formset.is_valid():
             #   book_formset.save()
            #return redirect('/index/')

    return render_to_response('blog_page.html')




def index(request):
    return HttpResponse("Hello, world. You're at the blog index.")

def blog_page(request):
    return render_to_response('blog/blog_page.html')

def vote(request):
    return HttpResponse("You're voting on question")

def cost(request):
    return HttpResponse("You're costing on question")