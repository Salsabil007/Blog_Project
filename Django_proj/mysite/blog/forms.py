from django import forms
from django.forms import ModelForm
from blog.models import Author


class AuthorForm(forms.ModelForm):
    name=forms.CharField(max_length=100)
    class Meta:
        model = Author
        fields=['name']

