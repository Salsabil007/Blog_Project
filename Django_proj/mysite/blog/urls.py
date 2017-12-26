from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^addblog/$', views.add_bloginfo,name='add_bloginfo' ),
    url(r'^(?P<aaa_id>\d+)/addcontent/$', views.add_content,name='add_content' ),
]