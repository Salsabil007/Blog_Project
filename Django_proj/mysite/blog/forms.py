from django.forms import ModelForm
from .models import Blog_Table, Blog_Part

class BlogForm(ModelForm):

    class Meta:
        model = Blog_Table
        fields = ['blog_title','blog_slug']

class ContentForm(ModelForm):

    class Meta:

        model=Blog_Part
        exclude = ("blogID",)
        fields= ['part_title','slug','Content']