from django.conf.urls import url

from . import views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.add_blog,name='add_blog' ),
]