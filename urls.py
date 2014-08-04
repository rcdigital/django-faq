from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^page/(?P<page>(.*?))/$', views.page,name='page' ),
    url(r'^(?P<slug>(.*?))/$', views.detail, name='detail')

)
