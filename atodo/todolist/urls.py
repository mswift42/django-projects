from django.conf.urls import patterns, url

from todolist import views

urlpatterns = patterns('',
                       url(r'^report', views.status_two, name='report'),
                       url(r'^$', views.index, name='index')
)


