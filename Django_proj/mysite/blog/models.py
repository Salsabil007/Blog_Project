from django.db import models
from django.contrib.auth.models import User



class Blog_Table(models.Model):
    userID= models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=200, unique=True)
    #Is_published=models.BooleanField(initial=True)
    blog_slug=models.CharField(max_length=200, unique=True)
    creation_timestamp=models.DateField(db_index=True, auto_now_add=True)
    modified_timestamp=models.DateField(db_index=True, auto_now_add=True)


class Blog_Part(models.Model):
    blogID=models.ForeignKey(Blog_Table, on_delete=models.CASCADE)
    date_of_creation = models.DateField(db_index=True, auto_now_add=True)
    Last_Modified= models.DateField(db_index=True, auto_now_add=True)
    Content = models.TextField()

    