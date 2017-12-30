from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index2/$', views.index2, name='index2'),
    url(r'^addblog/$', views.add_bloginfo,name='add_bloginfo' ),
    url(r'^(?P<aaa_id>\d+)/addcontent/$', views.add_content,name='add_content' ),
    url(r'^(?P<table_id>\d+)/(?P<part_id>\d+)/getcontent/$',views.get_content,name='get_content' ),
    url(r'^(?P<table_id>\d+)/(?P<part_id>\d+)/updateblog/$',views.update_blog,name='update_blog' ),
]