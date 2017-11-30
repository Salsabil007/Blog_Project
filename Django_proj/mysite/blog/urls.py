from django.conf.urls import url
from blog.views import HomeView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog_page/$', views.blog_page, name='blog_page'),
    url(r'^vote/$', views.vote, name='vote'),
    url(r'^cost/$', views.cost, name='cost'),
    url(r'^addbook/$', views.addbook, name='addbook'),
    url(r'^vi/$', HomeView.as_view(), name='home'),
    #url(r'^get_name/$', views.get_name, name='get_name'),


]