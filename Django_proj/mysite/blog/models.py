from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError

# Create your models here.


class Blog_Table(models.Model):
    #userID= models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=200, unique=True)
    #Is_published=models.BooleanField(initial=True)
    blog_slug=models.CharField(max_length=200, unique=True)
    creation_timestamp=models.DateField(db_index=True, auto_now_add=True)
    modified_timestamp=models.DateField(db_index=True, auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.blog_title

    def get_absolute_url(self):
        return 'view_blog_post', None, { 'slug': self.blog_slug }


class Blog_Part(models.Model):
    blogID=models.ForeignKey(Blog_Table, on_delete=models.CASCADE)
    part_title = models.CharField(max_length=200, unique=True)
    date_of_creation = models.DateField(db_index=True, auto_now_add=True)
    Last_Modified= models.DateField(db_index=True, auto_now_add=True)
    slug = models.CharField(max_length=200, unique=True)
    Content = models.TextField()

    def __unicode__(self):
        return '%s' % self.part_title

    def get_absolute_url(self):
        return 'view_blog_category', None, {'slug': self.slug}

